from delta.tables import DeltaTable


def merge_table(spark, df, metadata):
    """
    Generic MERGE utility for incremental loads.
    """

    target_table = (
        f"{metadata.target_catalog}."
        f"{metadata.target_schema}."
        f"{metadata.target_table}"
    )

    primary_key = metadata.primary_key

    if not spark.catalog.tableExists(target_table):
        (
            df.write
            .format("delta")
            .mode("overwrite")
            .saveAsTable(target_table)
        )
        return

    delta_table = DeltaTable.forName(spark, target_table)
    
    merge_condition = (
        f"target.{primary_key} = source.{primary_key}"
    )

    (
        delta_table.alias("target")
        .merge(
            df.alias("source"),
            merge_condition
        )
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute()
    )