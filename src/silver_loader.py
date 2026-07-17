from framework.metadata_reader import get_metadata
from framework.validator import validate_not_empty
from framework.logger import log_pipeline


def run_silver(spark, dataset):

    try:

        metadata = get_metadata(spark, dataset)

        bronze_table = (
            f"{metadata.target_catalog}."
            f"{metadata.target_schema}."
            f"{metadata.target_table}"
        )

        silver_table = bronze_table.replace(".bronze.", ".silver.")

        df = spark.table(bronze_table)

        validate_not_empty(df)

        silver_df = df.dropDuplicates()

        (
            silver_df.write
            .format("delta")
            .mode("overwrite")
            .saveAsTable(silver_table)
        )

        log_pipeline(
            spark,
            dataset,
            "Silver",
            "SUCCESS",
            silver_df.count(),
            "Silver Load Completed"
        )

    except Exception as e:

        log_pipeline(
            spark,
            dataset,
            "Silver",
            "FAILED",
            0,
            str(e)
        )

        raise