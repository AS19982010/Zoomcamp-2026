# NYC Taxi Data Ingestion Pipeline (dlt Workshop)

This repository contains my solution for the **dlt (data load tool) Workshop** as part of the **Data Engineering Zoomcamp 2026**. The project demonstrates how to build a production-ready data pipeline that extracts data from a REST API and loads it into an analytical database.



## 🎯 Objectives
The goal was to extract NYC Yellow Taxi trip data from a paginated JSON API and perform exploratory data analysis using SQL.

## 🛠️ Technical Challenges Solved
* **API Pagination**: Built a Python generator to handle stateful pagination (fetching 1,000 records per page until no more data was returned).
* **SSL Handshake Fix**: Resolved macOS-specific `CERTIFICATE_VERIFY_FAILED` errors by configuring a secure SSL context within the script.
* **Schema Evolution**: Used `dlt` to automatically normalize JSON responses into structured DuckDB tables.
* **Data Type Handling**: Handled a specific case where `payment_type` was returned as a string (`'Credit'`) instead of an integer, requiring custom SQL logic for aggregation.

## 🚀 How to Run

1. **Clone the repository and enter the directory:**
   ```bash
   cd data-engineering-zoomcamp/cohorts/2026/workshops/dlt

2. **Activate the virtual environment** 

source dlt_env/bin/activate
3. **Install dependencies:** 
pip install "dlt[duckdb]" pandas requests pyarrow duckdb

3. **Run the pipeline:** 
python3 solution.py

##  📊 Homework Results

Question 1	Dataset Date Range	2024-06-01 to 2024-07-01
Question 2	Credit Card Payment %	46.66%
Question 3	Total Tips Generated	$10,063.41

## 📝 Troubleshooting Note
During development, I encountered an issue where the payment_type column contained string values. I adjusted the SQL logic to use:

SQL
count(CASE WHEN payment_type = 'Credit' THEN 1 END)
This ensured the credit card proportion was calculated accurately despite the non-numeric data format.