#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click

def ingest_zones(engine):
    print("Downloading zone lookup data...")
    z_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"
    df_zones = pd.read_csv(z_url)
    
    print("Ingesting zones to Postgres...")
    df_zones.to_sql(name='zones', con=engine, if_exists='replace')
    print("Zones ingestion complete!")

def ingest_data(url: str, engine, target_table: str):
    print(f"Downloading data from {url}...")
    # Parquet jest wydajny, więc wczytujemy całość naraz (dla 1 miesiąca)
    df = pd.read_parquet(url)
    
    print(f"Ingesting data to table {target_table}...")
    # Tworzymy tabelę i wstawiamy dane
    df.to_sql(name=target_table, con=engine, if_exists="replace")
    print(f"Done ingesting {len(df)} rows to {target_table}")

@click.command()
@click.option('--pg_user', default='postgres', help='PostgreSQL username')
@click.option('--pg_pass', default='postgres', help='PostgreSQL password')
@click.option('--pg_host', default='postgres', help='PostgreSQL host')
@click.option('--pg_port', default='5432', help='PostgreSQL port')
@click.option('--pg_db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--year', default=2025, type=int, help='Year of the data')
@click.option('--month', default=11, type=int, help='Month of the data')
@click.option('--target_table', default='green_taxi_2025_11', help='Target table name')
def main(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, target_table):
    
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # Nowy URL do plików Parquet dla Green Taxi
    url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year:04d}-{month:02d}.parquet'

    # 1. Ładowanie danych Green Taxi
    ingest_data(url=url, engine=engine, target_table=target_table)

    # 2. Ładowanie stref
    ingest_zones(engine)

if __name__ == '__main__':
    main()