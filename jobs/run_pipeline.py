from pyspark.sql import SparkSession
from framework.orchestrator import run_pipeline

spark = SparkSession.builder.getOrCreate()

metadata_df = spark.sql("""
SELECT DISTINCT dataset_name
FROM consumerbank.metadata.ingestion_config
WHERE active_flag = 'Y'
ORDER BY dataset_name
""")

datasets = [row.dataset_name for row in metadata_df.collect()]

for dataset in datasets:  
    print("=" * 70)
    print(f"Starting pipeline for {dataset}")
    print("=" * 70) 
    run_pipeline(
        spark=spark,
        dataset=dataset
    )