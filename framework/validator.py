from pyspark.sql.functions import col


def validate_not_empty(df):

    if df.count() == 0:
        raise Exception("Input dataframe is empty")


def validate_column(df, column):

    if column not in df.columns:
        raise Exception(f"{column} not found")