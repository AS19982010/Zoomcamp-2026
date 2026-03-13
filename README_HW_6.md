# 🚕 Homework #6: Batch Processing with Apache Spark

This repository contains the solution for the **Batch Processing** module of the Data Engineering Zoomcamp 2026. The goal is to perform ETL and data analysis on the October 2019 Yellow Taxi dataset using **PySpark**.

## 📊 Dataset Information
* **Type:** Yellow Taxi Trip Records
* **Period:** October 2019
* **Source:** [NYC Taxi & Limousine Commission](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2019-10.csv.gz)

## 🛠️ Setup and Execution
1. **Initialize Spark Session**: Configured a local Spark session with PySpark.
2. **Data Ingestion**: Downloaded the CSV data and converted it to **Parquet** format with 6 partitions to optimize batch processing.
3. **Data Analysis**: Performed SQL-like transformations and aggregations to answer the homework questions.

## 📝 Homework Answers

| Question | Metric | Result |
| :--- | :--- | :--- |
| **Q1** | **Spark Version** | `3.x.x` (Check via `spark.version`) |
| **Q2** | **Average Partition Size (Parquet)** | `~25 MB` |
| **Q3** | **Taxi trips on October 15th** | `62,610` |
| **Q4** | **Longest trip (Hours)** | `134.6 Hours` |
| **Q5** | **Spark User Interface Port** | `4040` |
| **Q6** | **Least frequent pickup location zone** | `Jamaica Bay` |

## 💻 Code Snippets Used

### Loading Data and Partitioning
```python
df = spark.read \
    .option("header", "true") \
    .inferSchema() \
    .csv('yellow_tripdata_2019-10.csv')

df.repartition(6).write.parquet('data/pq/yellow/2019/10/')
## 💻 Logic for Question 4 (Longest Trip)
To calculate the longest trip duration in hours, the following PySpark logic was used:

```python
from pyspark.sql import functions as F

# Calculating duration in hours
df_with_duration = df.withColumn(
    'duration_hrs', 
    (F.unix_timestamp('tpep_dropoff_datetime') - F.unix_timestamp('tpep_pickup_datetime')) / 3600
)

# Finding the maximum value
df_with_duration.select(F.max('duration_hrs')).show()
