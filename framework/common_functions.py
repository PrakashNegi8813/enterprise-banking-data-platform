from pyspark.sql.functions import current_timestamp, lit


def add_audit_columns(df, pipeline_name, source_system):
    """
    Adds common audit columns.
    """

    return (
        df.withColumn("load_timestamp", current_timestamp())
          .withColumn("pipeline_name", lit(pipeline_name))
          .withColumn("source_system", lit(source_system))
    )