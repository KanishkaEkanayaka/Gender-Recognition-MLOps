import os
import urllib.request as request
import zipfile
import gdown
from cnnGenderClassifier.utils import logger
from cnnGenderClassifier.utils.common import get_size
from cnnGenderClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # download file from the location
    def download_file(self) -> str:
        """Fetch data from the URL
        """

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} to the file {zip_download_dir}")

            file_id = dataset_url.split("/")[5]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    
    # extract the zipfile
    def extract_zip_file(self):
        """
        zip file path: str
        Extracts the zip file into the data directory
        Function returns none
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)