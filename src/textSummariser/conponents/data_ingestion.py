import os
#for reading data from the url
import urllib.request as request
#for unzipping the dowloaded data
import zipfile
from textSummariser.logging import logger
from textSummariser.utils.common import get_size
from pathlib import Path
from textSummariser.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config



    #downloading file    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                #reading the source url
                url = self.config.source_URL,
                #giving the file location
                filename = self.config.local_data_file
            )
            #logger message
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            #getting the file size
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            
            
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
         