
# Data Engineering Zoomcamp 2026 - Homework Module 1

## Question 1 & 2
* **Question 1**: Answer is `25.3` (verified with `pip --version`)
* **Question 2**: Hostname and port: `db:5432`

## SQL Queries (Questions 3-6)

### Question 3: Counting short trips
```sql
SELECT COUNT(*) 
FROM green_taxi_2025_11
WHERE lpep_pickup_datetime >= '2025-11-01' 
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1; 
``` 
### Question 4: Longest trip distance
```SQL
SELECT 
    DATE(lpep_pickup_datetime) AS pickup_day,
    MAX(trip_distance) AS max_dist
FROM green_taxi_2025_11
WHERE trip_distance < 100
GROUP BY pickup_day
ORDER BY max_dist DESC
LIMIT 1; 
``` 
Question 5: Largest total_amount
```SQL
SELECT 
    z."Zone",
    SUM(g.total_amount) AS total_sum
FROM green_taxi_2025_11 g
JOIN zones z ON g."PULocationID" = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_sum DESC
LIMIT 1;
``` 
Question 6: Largest tip
```SQL
SELECT 
    zdo."Zone" AS dropoff_zone,
    MAX(g.tip_amount) AS max_tip
FROM green_taxi_2025_11 g
JOIN zones zpu ON g."PULocationID" = zpu."LocationID"
JOIN zones zdo ON g."DOLocationID" = zdo."LocationID"
WHERE zpu."Zone" = 'East Harlem North'
GROUP BY dropoff_zone
ORDER BY max_tip DESC
LIMIT 1; 
```

## Question 7. Terraform Workflow 
I successfully initialized and applied the infrastructure. 

**Terminal Output for `terraform apply`:**
```text
google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.demo-bucket: Creating...
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.