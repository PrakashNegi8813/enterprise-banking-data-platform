from pyspark.sql.functions import col


METADATA_TABLE = "consumerbank.metadata.ingestion_config"


def get_metadata(spark, dataset_name, layer):

    df = (
        spark.table(METADATA_TABLE)
        .filter(
            (col("dataset_name") == dataset_name)
            & (col("layer") == layer)
            & (col("active_flag") == "Y")
        )
    )

    rows = df.collect()

    if len(rows) == 0:
        raise Exception(
            f"No metadata found for Dataset={dataset_name}, Layer={layer}"
        )

    if len(rows) > 1:
        raise Exception(
            f"Multiple active metadata rows found for Dataset={dataset_name}, Layer={layer}"
        )

    return rows[0]