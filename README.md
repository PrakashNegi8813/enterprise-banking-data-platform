# Enterprise Banking Data Platform – Metadata-Driven ETL Framework

## Overview

This project demonstrates a production-style, metadata-driven ETL framework built on **Azure Databricks** using the **Medallion Architecture (Bronze, Silver, Gold)**.

The framework is designed to ingest data from Azure Data Lake Storage (ADLS), perform data validation and transformation, and publish curated Delta tables using a reusable, metadata-driven approach.

The objective is to onboard new datasets through metadata configuration with minimal code changes.

---

# Architecture

```
                Azure Data Lake Storage (ADLS)
                           │
                           ▼
                  Landing Source Files
                           │
                           ▼
                Bronze Layer (Raw Data)
                           │
                           ▼
           Silver Layer (Validated & Cleansed)
                           │
                           ▼
         Gold Layer (Business Ready Datasets)
                           │
                           ▼
             Reporting / Analytics / BI
```

---

# Technology Stack

- Azure Databricks
- PySpark
- Delta Lake
- Unity Catalog
- Azure Data Lake Storage Gen2 (ADLS)
- Python
- SQL
- Git & GitHub

---

# Key Features

- Metadata-driven ETL Framework
- Medallion Architecture (Bronze, Silver, Gold)
- Generic framework components
- Full & Incremental Load support
- Delta MERGE for incremental processing
- Watermark-based incremental loading
- Generic data validation framework
- Data quality checks
- Rejected record handling
- Pipeline audit logging
- Configuration-driven processing
- Reusable and extensible design

---

# Project Structure

```
enterprise-banking-data-platform/

│
├── configs/
│
├── framework/
│   ├── context.py
│   ├── exception_handler.py
│   ├── logger.py
│   ├── merge_writer.py
│   ├── metadata_reader.py
│   ├── quality_checker.py
│   ├── rejection_handler.py
│   ├── source_reader.py
│   ├── table_writer.py
│   ├── transformer.py
│   ├── validator.py
│   └── watermark.py
│
├── jobs/
│
├── metadata/
│
├── src/
│   ├── bronze_loader.py
│   ├── silver_loader.py
│   └── gold_loader.py
│
└── README.md
```

---

# Metadata-Driven Design

Pipeline execution is controlled through metadata.

Each dataset is configured using metadata including:

- Source Container
- Source Path
- Source File
- Target Catalog
- Target Schema
- Target Table
- Load Type
- Primary Key
- Watermark Column
- File Format

This allows new datasets to be onboarded without modifying the framework code.

---

# Processing Flow

## Bronze Layer

- Reads source files from ADLS
- Performs schema validation
- Adds ingestion metadata
- Loads raw Delta tables

---

## Silver Layer

- Reads Bronze tables
- Applies watermark filtering for incremental loads
- Performs data validation and quality checks
- Handles rejected records
- Uses Delta MERGE for incremental processing

---

## Gold Layer

- Reads Silver tables
- Applies business transformations
- Publishes curated business-ready datasets

---

# Audit Logging

Every pipeline execution captures:

- Batch ID
- Dataset Name
- Layer
- Start Time
- End Time
- Rows Read
- Rows Written
- Rows Rejected
- Pipeline Status

---

# Incremental Processing

Incremental datasets are processed using:

- Watermark-based filtering
- Metadata-driven primary keys
- Delta MERGE (UPSERT)

This minimizes data movement while ensuring data consistency.

---

# Data Quality

The framework supports:

- Primary Key Validation
- Duplicate Detection
- Null Validation
- Rejected Record Handling

---

# Sample Datasets

The project currently demonstrates the framework using:

- Branch Master
- Product Master

The framework can be extended to additional datasets through metadata configuration.

---

# Future Enhancements

- Azure Data Factory orchestration
- CI/CD using Azure DevOps
- Automated unit testing
- Slowly Changing Dimension (SCD Type 2)
- Change Data Capture (CDC)
- Pipeline monitoring dashboard
- Email notifications and alerting

---

# How to Run

1. Upload source files to the Landing container in ADLS.
2. Configure dataset metadata in the metadata tables.
3. Execute the pipeline:

```python
from framework.orchestrator import run_pipeline

run_pipeline(
    spark=spark,
    dataset="branch"
)
```

The framework automatically executes:

- Bronze Load
- Silver Load
- Gold Load

based on the metadata configuration.

---

# Author

**Prakash Negi**

Senior Data & Analytics Professional

- 15+ years of experience in Analytics, Data Engineering, Risk Reporting, Regulatory Reporting and Enterprise Data Platforms
- Technologies: Azure Databricks, PySpark, SQL, Python, Delta Lake, Azure Data Factory, Power BI