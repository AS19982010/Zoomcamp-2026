import dlt
import duckdb
import requests
import ssl

# Naprawa SSL na Macu
ssl._create_default_https_context = ssl._create_unverified_context

@dlt.resource(name="taxi_data", write_disposition="replace")
def nyc_taxi_api():
    url = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"
    page = 1
    while True:
        params = {"page": page}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        yield data
        print(f"Pobrano stronę {page}")
        page += 1

pipeline = dlt.pipeline(
    pipeline_name="nyc_taxi_pipeline",
    destination="duckdb",
    dataset_name="taxi_dataset"
)

pipeline.run(nyc_taxi_api())

conn = duckdb.connect("nyc_taxi_pipeline.duckdb")

print("\n" + "="*50)
print("WYNIKI DLA TWOJEJ PRACY DOMOWEJ:")

# Pytanie 1: Zakres dat
dates = conn.execute("SELECT min(trip_pickup_date_time), max(trip_pickup_date_time) FROM taxi_dataset.taxi_data").fetchone()

# Pytanie 2: Proporcja płatności kartą - szukamy tekstu 'Credit' zamiast liczby 1
stats = conn.execute("""
    SELECT 
        count(*), 
        count(CASE WHEN payment_type = 'Credit' THEN 1 END)
    FROM taxi_dataset.taxi_data
""").fetchone()

total_trips = stats[0]
cc_trips = stats[1]
cc_percent = (cc_trips / total_trips) * 100

# Pytanie 3: Suma napiwków
tips = conn.execute("SELECT sum(tip_amt) FROM taxi_dataset.taxi_data").fetchone()[0]

print(f"Pytanie 1 (Daty): {dates[0]} do {dates[1]}")
print(f"Pytanie 2 (Karta Kredytowa %): {cc_percent:.2f}%")
print(f"Pytanie 3 (Suma napiwków): ${tips:,.2f}")
print("="*50 + "\n")
