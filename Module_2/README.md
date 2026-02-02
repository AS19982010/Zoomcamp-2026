
# 📊 NYC Taxi Data Pipeline - Module 2 Homework

This repository contains my solution for the **Data Engineering Zoomcamp 2026 - Module 2**, focusing on Workflow Orchestration with **Kestra**.

The goal of this assignment was to manage and orchestrate an ETL pipeline for the NYC Taxi dataset (Yellow and Green) using Google Cloud Platform and Kestra's advanced features like backfilling and scheduling.

## 🚀 Key Implementation Details

* **Workflow Orchestration**: Built robust Kestra flows to automate data extraction, transformation, and loading (ETL).
* **Infrastructure as Code (IaC)**: Configured the local environment using **Docker Compose**, including a Kestra instance with **Gemini AI Copilot** integration.
* **Secure Variable Management**: Utilized Kestra's **KV Store** to securely manage GCP project IDs, dataset locations, and credentials.
* **Data Backfill**: Performed a full backfill for the year 2021 (Jan-Jul) for both taxi services, ensuring data consistency across multiple months.

## 🖼️ Documentation & Screenshots

### 🗺️ Pipeline Topology
Visualization of the data flow architecture.
![Topology](Module_2/images/Modul_2_1.png)

### ⚙️ Docker & Environment Setup
Configuration for Kestra with Gemini AI support enabled.
Module_2/images/Modul%202.2.png

### 🔐 Variable Management (KV Store)
Centralized configuration for GCP project settings and API keys.
![KV Store Configuration](Module_2/images/Modul%202.4.png)

### 🚥 Execution History & Backfill Status
Confirmation of successful pipeline runs for historical data processing.
![Execution Status](Module_2/images/Modul%202.5.png)

## 📝 Quiz Results Summary

Based on the pipeline executions and BigQuery analysis, here are the findings for the homework assignment:

1. **Yellow Taxi (Dec 2020) Size**: 128.3 MiB.

2. **Rendered File Name**: `green_tripdata_2020-04.csv`.
3. **Yellow Taxi 2020 Row Count**: 24,648,499.
4. **Green Taxi 2020 Row Count**: 1,734,051.
5. **Yellow Taxi March 2021 Row Count**: 1,925,152.
6. **Timezone Configuration**: Used `America/New_York` for accurate scheduling.

