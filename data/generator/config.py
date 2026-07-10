"""
===============================================================================
Project : Enterprise Complaints Reporting Platform
Module  : Configuration
Purpose : Central configuration for all data generators
Author  : Prakash Negi
===============================================================================
"""

from pathlib import Path

# ==============================================================================
# Project Paths
# ==============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_SYSTEM_FOLDER = PROJECT_ROOT / "source_systems"

GENERATED_DATA_FOLDER = PROJECT_ROOT / "generated_data"

LANDING_FOLDER = GENERATED_DATA_FOLDER / "landing"

BRONZE_FOLDER = GENERATED_DATA_FOLDER / "bronze"

SILVER_FOLDER = GENERATED_DATA_FOLDER / "silver"

GOLD_FOLDER = GENERATED_DATA_FOLDER / "gold"

LOG_FOLDER = GENERATED_DATA_FOLDER / "logs"

ARCHIVE_FOLDER = GENERATED_DATA_FOLDER / "archive"

TEMP_FOLDER = GENERATED_DATA_FOLDER / "temp"

# ==============================================================================
# Landing Folders
# ==============================================================================

CUSTOMER_FOLDER = LANDING_FOLDER / "customer"

DEPOSIT_ACCOUNT_FOLDER = LANDING_FOLDER / "deposit_account"

LOAN_ACCOUNT_FOLDER = LANDING_FOLDER / "loan_account"

TRANSACTION_FOLDER = LANDING_FOLDER / "transaction"

PRODUCT_FOLDER = LANDING_FOLDER / "product"

BRANCH_FOLDER = LANDING_FOLDER / "branch"

CUSTOMER_SEGMENT_FOLDER = LANDING_FOLDER / "customer_segment"

COMPLAINT_FOLDER = LANDING_FOLDER / "complaint"

COMPLAINT_TRANSCRIPT_FOLDER = LANDING_FOLDER / "complaint_transcript"

# ==============================================================================
# Data Volume
# ==============================================================================

NUMBER_OF_CUSTOMERS = 50000

NUMBER_OF_BRANCHES = 100

NUMBER_OF_PRODUCTS = 20

NUMBER_OF_DEPOSIT_ACCOUNTS = 65000

NUMBER_OF_LOAN_ACCOUNTS = 18000

NUMBER_OF_TRANSACTIONS = 2000000

NUMBER_OF_COMPLAINTS = 250000

# ==============================================================================
# Random Seed
# ==============================================================================

RANDOM_SEED = 2026