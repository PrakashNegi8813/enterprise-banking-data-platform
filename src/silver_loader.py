from framework.source_reader import read_source
from framework.table_writer import write_table
from framework.logger import log_pipeline
from framework.rejection_handler import save_rejected_records

from framework.transformer import (
    standardize_column_names,
    trim_string_columns,
    remove_duplicates
)

from framework.quality_checker import (
    validate_primary_key,
    split_duplicate_records
)

from framework.watermark import (
    get_last_watermark,
    apply_watermark
)


def load_silver(spark, dataset, context, metadata):

    start_time = context["start_time"]

    df = read_source(
        spark,
        metadata
    )

    rows_read = df.count()

    if metadata.load_type.upper() == "INCREMENTAL":

        watermark = get_last_watermark(
            spark,
            metadata
        )

        df = apply_watermark(
            df,
            metadata,
            watermark
        )

    df = standardize_column_names(df)

    df = trim_string_columns(df)

    df = remove_duplicates(df)

    validate_primary_key(
        df,
        metadata.primary_key
    )

    df, rejected = split_duplicate_records(
        df,
        metadata.primary_key
    )

    rows_rejected = rejected.count()

    if rows_rejected > 0:

        save_rejected_records(
            rejected,
            metadata.dataset_name,
            metadata.layer,
            context["batch_id"],
            "Duplicate Primary Key"
        )

    write_table(
        spark,
        df,
        metadata
    )

    rows_written = df.count()

    log_pipeline(
        spark=spark,
        dataset=dataset,
        layer="SILVER",
        batch_id=context["batch_id"],
        status="SUCCESS",
        rows_read=rows_read,
        rows_written=rows_written,
        rows_rejected=rows_rejected,
        start_time=start_time,
        message="Silver load completed successfully."
    )