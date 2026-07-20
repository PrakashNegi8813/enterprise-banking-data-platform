from framework.merge_writer import merge_table


def write_table(spark, df, metadata):
    """
    Write data using FULL or INCREMENTAL load.
    """

    target_table = (
        f"{metadata.target_catalog}."
        f"{metadata.target_schema}."
        f"{metadata.target_table}"
    )

    load_type = metadata.load_type.upper()

    if load_type == "FULL":

        (
            df.write
            .format("delta")
            .mode("overwrite")
            .option("overwriteSchema", "true")
            .saveAsTable(target_table)
        )

    elif load_type == "INCREMENTAL":

        merge_table(
            spark,
            df,
            metadata
        )

    else:

        raise Exception(
            f"Unsupported Load Type : {load_type}"
        )