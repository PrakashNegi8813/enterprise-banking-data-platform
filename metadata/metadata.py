import json

# Metadata configuration
metadata = [
    {
        "SourceName": "branch",
        "FileName": "branch",
        "SourceContainer": "landing",
        "TargetContainer": "bronze",
        "TargetTable": "branch",
        "LoadType": "Full",
        "Notebook": "01_Bronze_Ingestion",
        "IsActive": True
    },
    {
        "SourceName": "product",
        "FileName": "product",
        "SourceContainer": "landing",
        "TargetContainer": "bronze",
        "TargetTable": "product",
        "LoadType": "Full",
        "Notebook": "01_Bronze_Ingestion",
        "IsActive": True
    }
]

# ADLS path
metadata_path = "abfss://metadata@stconsumerbankdev001.dfs.core.windows.net/metadata.json"

# Write JSON to ADLS
dbutils.fs.put(
    metadata_path,
    json.dumps(metadata, indent=4),
    overwrite=True
)

print(f"Metadata file created successfully at:\n{metadata_path}")