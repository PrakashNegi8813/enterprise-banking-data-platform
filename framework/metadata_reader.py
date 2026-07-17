def get_metadata(spark, dataset_name):

    query = f"""
    SELECT *
    FROM consumerbank.metadata.ingestion_config
    WHERE dataset_name='{dataset_name}'
    """

    return spark.sql(query).first() 