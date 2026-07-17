from framework.metadata_reader import get_metadata
from framework.validator import validate_not_empty
from framework.logger import log_pipeline


def run_gold(spark, dataset):

    try:

        metadata = get_metadata(spark, dataset)

        silver_table = (
            f"{metadata.target_catalog}.silver.{metadata.target_table}"
        )

        gold_table = (
            f"{metadata.target_catalog}.gold.{metadata.target_table}"
        )

        df = spark.table(silver_table)

        validate_not_empty(df)

        (
            df.write
            .format("delta")
            .mode("overwrite")
            .saveAsTable(gold_table)
        )

        log_pipeline(
            spark,
            dataset,
            "Gold",
            "SUCCESS",
            df.count(),
            "Gold Load Completed"
        )

    except Exception as e:

        log_pipeline(
            spark,
            dataset,
            "Gold",
            "FAILED",
            0,
            str(e)
        )

        raise