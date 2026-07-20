from configs.environment import STORAGE_ACCOUNT


def read_source(spark, metadata):

    if metadata.source_type == "FILE":

        if metadata.source_file and metadata.source_file.strip():

            # Read a specific file
            path = (
                f"abfss://{metadata.source_container}"
                f"@{STORAGE_ACCOUNT}.dfs.core.windows.net/"
                f"{metadata.source_path.rstrip('/')}/"
                f"{metadata.source_file}"
            )

        else:

            # Read all files in the folder
            path = (
                f"abfss://{metadata.source_container}"
                f"@{STORAGE_ACCOUNT}.dfs.core.windows.net/"
                f"{metadata.source_path.rstrip('/')}/"
            )

        file_format = metadata.file_format.lower()

        if file_format == "parquet":

            df = spark.read.parquet(path)

        elif file_format == "csv":

            df = (
                spark.read
                .option("header", "true")
                .option("inferSchema", "true")
                .csv(path)
            )

        elif file_format == "json":

            df = spark.read.json(path)

        else:

            raise Exception(
                f"Unsupported file format : {metadata.file_format}"
            )

        return df

    elif metadata.source_type == "TABLE":

        table_name = (
            f"{metadata.source_catalog}."
            f"{metadata.source_schema}."
            f"{metadata.source_table}"
        )

        return spark.table(table_name)

    else:

        raise Exception(
            f"Unsupported Source Type : {metadata.source_type}"
        )