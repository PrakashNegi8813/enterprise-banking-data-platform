from pyspark.sql.functions import current_timestamp, lit, to_json, struct


def save_rejected_records(
    df,
    dataset,
    layer,
    batch_id,
    reason
):
    """
    Save rejected records into Delta table.
    """

    rejected_df = (
        df.withColumn("dataset", lit(dataset))
          .withColumn("layer", lit(layer))
          .withColumn("batch_id", lit(batch_id))
          .withColumn("rejected_reason", lit(reason))
          .withColumn("rejected_timestamp", current_timestamp())
          .withColumn(
              "record",
              to_json(struct(*df.columns))
          )
          .select(
              "dataset",
              "layer",
              "batch_id",
              "rejected_reason",
              "rejected_timestamp",
              "record"
          )
    )

    (
        rejected_df.write
        .mode("append")
        .saveAsTable(
            "consumerbank.metadata.rejected_records"
        )
    )