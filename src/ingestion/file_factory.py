from abc import ABC, abstractmethod


class FileReader(ABC):
    """Abstract base class for all file readers."""

    @abstractmethod
    def read(self, spark, path):
        pass


class CSVReader(FileReader):

    def read(self, spark, path):
        return (
            spark.read
            .option("header", True)
            .csv(path)
        )


class ParquetReader(FileReader):

    def read(self, spark, path):
        return spark.read.parquet(path)


class JSONReader(FileReader):

    def read(self, spark, path):
        return spark.read.json(path)


class SASReader(FileReader):

    def read(self, spark, path):
        raise NotImplementedError(
            "SAS Reader will be implemented later."
        )


class FileFactory:

    @staticmethod
    def get_reader(file_type):

        readers = {
            "csv": CSVReader(),
            "parquet": ParquetReader(),
            "json": JSONReader(),
            "sas": SASReader()
        }

        if file_type.lower() not in readers:
            raise ValueError(
                f"Unsupported file type : {file_type}"
            )

        return readers[file_type.lower()]