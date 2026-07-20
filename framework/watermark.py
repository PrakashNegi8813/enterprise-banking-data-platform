from pyspark.sql.functions import max, col


def get_last_watermark(spark, metadata):

    table_name = (
        f"{metadata.target_catalog}."
        f"{metadata.target_schema}."
        f"{metadata.target_table}"
    )

    if not metadata.watermark_column:
        return None

    try:

        value = (
            spark.table(table_name)
            .agg(
                max(col(metadata.watermark_column))
            )
            .collect()[0][0]
        )

        return value

    except Exception as e:
        print(f"Watermark not found: {e}")
        return None



def apply_watermark(df, metadata, watermark):

    if watermark is None:

        return df

    return df.filter(
        col(metadata.watermark_column) > watermark
    )