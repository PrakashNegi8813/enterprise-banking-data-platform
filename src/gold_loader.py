from framework.source_reader import read_source
from framework.table_writer import write_table
from framework.logger import log_pipeline


def load_gold(spark, dataset, context, metadata):

    start_time = context["start_time"]

    df = read_source(
        spark,
        metadata
    )

    rows_read = df.count()

    #
    # Business transformations go here
    #

    write_table(
        spark,
        df,
        metadata
    )

    rows_written = df.count()

    log_pipeline(
        spark=spark,
        dataset=dataset,
        layer="GOLD",
        batch_id=context["batch_id"],
        status="SUCCESS",
        rows_read=rows_read,
        rows_written=rows_written,
        rows_rejected=0,
        start_time=start_time,
        message="Gold load completed successfully."
    )