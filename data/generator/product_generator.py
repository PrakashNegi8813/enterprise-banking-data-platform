"""
===============================================================================
Project : Enterprise Complaints Reporting Platform
Module  : Product Generator
Purpose : Generate Product Master data for Consumer Banking
Author  : Prakash Negi
===============================================================================
"""

import logging
import time
from datetime import datetime

import pandas as pd

from config import PRODUCT_FOLDER

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


class ProductGenerator:

    def __init__(self):

        PRODUCT_FOLDER.mkdir(parents=True, exist_ok=True)

    def generate(self):

        logger.info("Generating Product Master...")

        products = [

            {
                "Product_ID": "PROD001",
                "Product_Code": "SAV001",
                "Product_Name": "Savings Account",
                "Product_Category": "Deposit",
                "Interest_Rate": 3.50,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD002",
                "Product_Code": "CUR001",
                "Product_Name": "Current Account",
                "Product_Category": "Deposit",
                "Interest_Rate": 0.00,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD003",
                "Product_Code": "FD001",
                "Product_Name": "Fixed Deposit",
                "Product_Category": "Deposit",
                "Interest_Rate": 6.75,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD004",
                "Product_Code": "HL001",
                "Product_Name": "Home Loan",
                "Product_Category": "Loan",
                "Interest_Rate": 8.50,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD005",
                "Product_Code": "PL001",
                "Product_Name": "Personal Loan",
                "Product_Category": "Loan",
                "Interest_Rate": 12.50,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD006",
                "Product_Code": "AL001",
                "Product_Name": "Auto Loan",
                "Product_Category": "Loan",
                "Interest_Rate": 9.25,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD007",
                "Product_Code": "ED001",
                "Product_Name": "Education Loan",
                "Product_Category": "Loan",
                "Interest_Rate": 8.90,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD008",
                "Product_Code": "CC001",
                "Product_Name": "Credit Card",
                "Product_Category": "Card",
                "Interest_Rate": 0.00,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD009",
                "Product_Code": "OD001",
                "Product_Name": "Overdraft",
                "Product_Category": "Credit",
                "Interest_Rate": 13.50,
                "Status": "Active"
            },

            {
                "Product_ID": "PROD010",
                "Product_Code": "MF001",
                "Product_Name": "Mutual Fund",
                "Product_Category": "Investment",
                "Interest_Rate": 0.00,
                "Status": "Active"
            }

        ]

        df = pd.DataFrame(products)

        df["Created_Date"] = datetime.now()
        df["Last_Updated_TS"] = datetime.now()

        return df

    def save(self, df):

        csv_path = PRODUCT_FOLDER / "product_master.csv"
        parquet_path = PRODUCT_FOLDER / "product_master.parquet"

        df.to_csv(csv_path, index=False)
        df.to_parquet(parquet_path, index=False)

        logger.info(f"CSV Saved      : {csv_path}")
        logger.info(f"Parquet Saved  : {parquet_path}")

    def run(self):

        start = time.time()

        logger.info("=" * 70)
        logger.info("Product Generator Started")

        df = self.generate()

        self.save(df)

        logger.info(f"Total Products : {len(df)}")
        logger.info(f"Execution Time : {round(time.time()-start,2)} seconds")
        logger.info("Product Generator Completed")
        logger.info("=" * 70)


if __name__ == "__main__":

    ProductGenerator().run()