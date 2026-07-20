from framework.source_reader import read_source
from framework.table_writer import write_table
from framework.validator import validate_not_empty
from framework.logger import log_pipeline

from pyspark.sql.functions import (
    current_timestamp,
    lit
)


def load_bronze(spark, dataset, context, metadata):

    start_time = context["start_time"]

    df = read_source(
        spark,
        metadata
    )

    rows_read = df.count()

    df = (
        df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("batch_id", lit(context["batch_id"]))
        .withColumn("pipeline_name", lit(context["pipeline_name"]))
    )

    validate_not_empty(df)

    write_table(
        spark,
        df,
        metadata
    )

    rows_written = df.count()

    log_pipeline(
        spark=spark,
        dataset=dataset,
        layer="BRONZE",
        batch_id=context["batch_id"],
        status="SUCCESS",
        rows_read=rows_read,
        rows_written=rows_written,
        rows_rejected=0,
        start_time=start_time,
        message="Bronze load completed successfully."
    )