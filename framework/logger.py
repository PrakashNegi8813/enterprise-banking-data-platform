from pyspark.sql.functions import current_timestamp


def log_pipeline(
    spark,
    dataset,
    layer,
    status,
    rows_processed,
    message
):

    spark.sql(f"""
        INSERT INTO consumerbank.metadata.pipeline_audit
        VALUES (
            '{dataset}',
            '{layer}',
            '{status}',
            {rows_processed},
            '{message}',
            current_timestamp()
        )
    """)