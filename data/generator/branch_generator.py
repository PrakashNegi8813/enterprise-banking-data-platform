"""
===============================================================================
Project : Enterprise Complaints Reporting Platform
Module  : Branch Generator
Purpose : Generate Branch Master data for Consumer Banking
Author  : Prakash Negi
===============================================================================
"""

import logging
import random
import time
from datetime import datetime

import pandas as pd

from config import (
    BRANCH_FOLDER,
    NUMBER_OF_BRANCHES,
    RANDOM_SEED,
)

# ------------------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# Master Data
# ------------------------------------------------------------------------------

REGIONS = {
    "North": ["Delhi", "Chandigarh", "Lucknow"],
    "South": ["Hyderabad", "Bangalore", "Chennai"],
    "West": ["Mumbai", "Pune", "Ahmedabad"],
    "East": ["Kolkata", "Bhubaneswar", "Patna"]
}

STATES = {
    "Delhi": "Delhi",
    "Chandigarh": "Chandigarh",
    "Lucknow": "Uttar Pradesh",
    "Hyderabad": "Telangana",
    "Bangalore": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat",
    "Kolkata": "West Bengal",
    "Bhubaneswar": "Odisha",
    "Patna": "Bihar"
}

BRANCH_TYPES = [
    "Retail",
    "Corporate",
    "Regional",
    "Digital"
]

STATUS = [
    "Active",
    "Active",
    "Active",
    "Active",
    "Closed"
]


class BranchGenerator:

    def __init__(self):

        random.seed(RANDOM_SEED)

        BRANCH_FOLDER.mkdir(parents=True, exist_ok=True)

    def generate(self):

        logger.info("Generating Branch Master Data...")

        rows = []

        branch_number = 1001

        for i in range(NUMBER_OF_BRANCHES):

            region = random.choice(list(REGIONS.keys()))
            city = random.choice(REGIONS[region])
            state = STATES[city]

            branch_id = f"BR{branch_number:04d}"

            rows.append({

                "Branch_ID": branch_id,

                "Branch_Code": f"{branch_number}",

                "Branch_Name": f"{city} Branch",

                "Region": region,

                "State": state,

                "City": city,

                "Address": f"{random.randint(10,999)} Main Road, {city}",

                "IFSC_Code": f"CBNK000{branch_number}",

                "Branch_Type": random.choice(BRANCH_TYPES),

                "Manager_ID": f"EMP{random.randint(10000,99999)}",

                "Status": random.choice(STATUS),

                "Open_Date": pd.Timestamp(
                    random.randint(2005, 2022),
                    random.randint(1, 12),
                    random.randint(1, 28)
                ),

                "Last_Updated_TS": datetime.now()

            })

            branch_number += 1

        return pd.DataFrame(rows)

    def save(self, df: pd.DataFrame):

        csv_path = BRANCH_FOLDER / "branch_master.csv"
        parquet_path = BRANCH_FOLDER / "branch_master.parquet"

        df.to_csv(csv_path, index=False)

        df.to_parquet(parquet_path, index=False)

        logger.info(f"CSV Saved      : {csv_path}")
        logger.info(f"Parquet Saved  : {parquet_path}")

    def run(self):

        start = time.time()

        logger.info("=" * 70)
        logger.info("Branch Generator Started")

        df = self.generate()

        self.save(df)

        logger.info(f"Total Branches : {len(df)}")
        logger.info(f"Execution Time : {round(time.time() - start,2)} seconds")
        logger.info("Branch Generator Completed")
        logger.info("=" * 70)


if __name__ == "__main__":

    BranchGenerator().run()