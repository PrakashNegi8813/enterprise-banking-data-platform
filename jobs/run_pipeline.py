from pyspark.sql import SparkSession
from framework.orchestrator import run_pipeline

spark = SparkSession.builder.getOrCreate()

datasets = [
    "branch",
    "product"
]

for dataset in datasets:
    run_pipeline(
        spark=spark,
        dataset=dataset
    )