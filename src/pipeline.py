from src.bronze_loader import run_bronze
from src.silver_loader import run_silver
from src.gold_loader import run_gold


def execute_pipeline(spark, dataset):

    run_bronze(spark, dataset)

    run_silver(spark, dataset)

    run_gold(spark, dataset)

    print(f"{dataset} pipeline completed successfully.")