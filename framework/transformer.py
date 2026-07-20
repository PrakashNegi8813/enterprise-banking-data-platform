from pyspark.sql.functions import col, trim
from pyspark.sql.types import StringType


def standardize_column_names(df):
    """
    Convert column names to lowercase and replace spaces with underscores.
    """

    for column in df.columns:
        df = df.withColumnRenamed(
            column,
            column.strip().lower().replace(" ", "_")
        )

    return df


def trim_string_columns(df):
    """
    Trim leading and trailing spaces from all string columns.
    """

    for field in df.schema.fields:

        if isinstance(field.dataType, StringType):

            df = df.withColumn(
                field.name,
                trim(col(field.name))
            )

    return df


def remove_duplicates(df):
    """
    Remove duplicate records.
    """

    return df.dropDuplicates()


def cast_columns(df, column_mapping):
    """
    Generic datatype casting.

    Example:
    {
        "amount":"double",
        "branch_id":"int"
    }
    """

    for column_name, datatype in column_mapping.items():

        if column_name in df.columns:

            df = df.withColumn(
                column_name,
                col(column_name).cast(datatype)
            )

    return df


def replace_nulls(df, replacements):
    """
    Replace null values.

    Example:
    {
        "state":"UNKNOWN",
        "city":"NA"
    }
    """

    return df.fillna(replacements)