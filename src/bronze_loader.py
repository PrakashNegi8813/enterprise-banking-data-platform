from framework.metadata_reader import get_metadata
from framework.common_functions import add_audit_columns
from framework.validator import validate_not_empty
from framework.logger import log_pipeline
from configs.config import *


def run_bronze(spark, dataset):

    try:

        metadata = get_metadata(spark, dataset)

        source_path = (
            f"abfss://{metadata.source_container}"
            f"@{STORAGE_ACCOUNT}.dfs.core.windows.net/"
            f"{metadata.source_path}"
        )

        df = spark.read.format(metadata.file_format).load(source_path)

        validate_not_empty(df)

        bronze_df = add_audit_columns(
            df,
            PIPELINE_NAME,
            SOURCE_SYSTEM
        )

        target_table = (
            f"{metadata.target_catalog}."
            f"{metadata.target_schema}."
            f"{metadata.target_table}"
        )

        (
            bronze_df.write
            .format("delta")
            .mode("overwrite")
            .saveAsTable(target_table)
        )

        row_count = bronze_df.count()

        log_pipeline(
            spark,
            dataset,
            "Bronze",
            "SUCCESS",
            row_count,
            "Bronze Load Completed"
        )

    except Exception as e:

        log_pipeline(
            spark,
            dataset,
            "Bronze",
            "FAILED",
            0,
            str(e)
        )

        raise