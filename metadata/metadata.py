metadata = [
    ("branch","branch","landing","bronze","branch","Full","01_Bronze_Ingestion",True),
    ("product","product","landing","bronze","product","Full","01_Bronze_Ingestion",True)
]

columns = [
    "SourceName",
    "FileName",
    "SourceContainer",
    "TargetContainer",
    "TargetTable",
    "LoadType",
    "Notebook",
    "IsActive"
]

df = spark.createDataFrame(metadata, columns)

df.coalesce(1).write.mode("overwrite").json(
    "abfss://metadata@stconsumerbankdev001.dfs.core.windows.net/metadata"
)