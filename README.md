# Consumer Banking Data Platform

## Overview

The Consumer Banking Data Platform is an enterprise-grade Azure data engineering project designed to simulate how a large bank processes, transforms, and serves analytical data.

The platform follows the Medallion Architecture (Bronze, Silver, Gold) and demonstrates end-to-end implementation using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, Delta Lake, Unity Catalog, GitHub, and Power BI.

Unlike tutorial projects, this repository is organized using enterprise software engineering practices, including documentation, metadata-driven ingestion, reusable Python modules, monitoring, logging, and CI/CD.

---

## Business Problem

Consumer Banking data originates from multiple operational systems such as Oracle, Teradata, SharePoint, SAS, and Enterprise Complaint platforms.

The objective is to build an independent Consumer Banking pipeline while consuming shared enterprise datasets (for example, Enterprise Complaint Silver) to avoid duplicate processing and maintain a single source of truth.

---

## Architecture

Enterprise Complaint Pipeline

Landing → Bronze → Silver

↓

Consumer Banking Pipeline

Landing → Bronze → Silver → Gold

↓

Power BI

---

## Technology Stack

- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Data Factory
- Delta Lake
- Unity Catalog
- PySpark
- Python
- GitHub
- Azure DevOps
- Power BI

---

## Project Status

🚧 Under Active Development