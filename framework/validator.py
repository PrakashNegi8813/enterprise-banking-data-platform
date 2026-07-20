from pyspark.sql.functions import col


def validate_not_empty(df):

    if df.head(1) == []:

        raise Exception("Input DataFrame is empty.")


def validate_column(df, column_name):

    if column_name not in df.columns:

        raise Exception(
            f"{column_name} not found."
        )