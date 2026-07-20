from datetime import datetime


def log_pipeline(
    spark,
    dataset,
    layer,
    batch_id,
    status,
    rows_read,
    rows_written,
    rows_rejected,
    start_time,
    message=""
):

    end_time = datetime.now()

    duration = (
        end_time - start_time
    ).total_seconds()

    spark.sql(f"""
    INSERT INTO consumerbank.metadata.pipeline_audit
    VALUES(
        '{dataset}',
        '{layer}',
        '{batch_id}',
        '{status}',
        {rows_read},
        {rows_written},
        {rows_rejected},
        TIMESTAMP('{start_time}'),
        TIMESTAMP('{end_time}'),
        {duration},
        '{message}'
    )
    """)