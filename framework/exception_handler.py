import traceback


def handle_exception(
    spark,
    dataset,
    layer,
    batch_id,
    ex
):

    message = traceback.format_exc()

    spark.sql(f"""
    INSERT INTO consumerbank.metadata.pipeline_audit
    VALUES(
        '{dataset}',
        '{layer}',
        '{batch_id}',
        'FAILED',
        0,
        0,
        0,
        current_timestamp(),
        current_timestamp(),
        0,
        '{message.replace("'", " ")}'
    )
    """)

    raise ex