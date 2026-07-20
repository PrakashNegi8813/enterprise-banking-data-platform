from pyspark.sql.functions import col


def validate_primary_key(df, primary_key):

    if primary_key not in df.columns:

        raise Exception(
            f"Primary Key '{primary_key}' not found."
        )

'''
def validate_duplicates(df, primary_key):

    duplicate_count = (
        df.groupBy(primary_key)
        .count()
        .filter(col("count") > 1)
        .count()
    )

    if duplicate_count > 0:

        raise Exception(
            f"Duplicate records found for '{primary_key}'."
        )
'''
def split_duplicate_records(df, primary_key):

    duplicate_keys = (
        df.groupBy(primary_key)
          .count()
          .filter(col("count") > 1)
          .select(primary_key)
    )

    rejected_df = df.join(
        duplicate_keys,
        primary_key,
        "inner"
    )

    valid_df = df.join(
        duplicate_keys,
        primary_key,
        "left_anti"
    )

    return valid_df, rejected_df

def validate_row_count(df):

    if df.count() == 0:

        raise Exception(
            "DataFrame contains zero records."
        )


def validate_nulls(df, column_name):

    null_count = (
        df
        .filter(col(column_name).isNull())
        .count()
    )

    if null_count > 0:

        raise Exception(
            f"{null_count} NULL values found in {column_name}"
        )