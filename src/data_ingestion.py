import os
import sys
import pandas as pd
from google.cloud import storage
from src.exception.exception_handling import CustomException
from src.logger.logger import get_logger
from src.utils.common_functions import read_yaml
from config.paths_config import *


logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_names = self.config["bucket_file_names"]

        os.makedirs(RAW_DIR, exist_ok=True)
        logger.info("Data Ingestion Class Configured")

    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file in self.file_names:
                save_path = os.path.join(RAW_DIR, file)

                if file == "animelist.csv":
                    blob = bucket.blob(file)
                    blob.download_to_filename(save_path)

                    # Limit rows for large file
                    data = pd.read_csv(save_path, nrows=5000000)
                    data.to_csv(save_path, index=False)
                    logger.info(f"Large file '{file}' detected, saved first 5M rows in {save_path}")
                else:
                    blob = bucket.blob(file)
                    blob.download_to_filename(save_path)
                    logger.info(f"{file} downloaded to {save_path}")

            client.close()
            logger.info("All CSV files downloaded from GCP Bucket successfully and client closed.")

        except Exception as e:
            logger.error("Error occurred while importing CSV from Google Cloud.")
            raise CustomException(e, sys)

    def run(self):
        try:
            logger.info("Starting Data Ingestion Process...")
            self.download_csv_from_gcp()
            logger.info("Data Ingestion completed successfully.")
        except Exception as e:
            logger.error("Error while running Data Ingestion.")
            raise CustomException(e, sys)


if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()
