from textSummariser.config.configuration import ConfigurationManager
#responsible for managing the configuration settings. it might load configuration data from files
from textSummariser.conponents.data_ingestion import DataIngestion
# responsible for handiling data ingestion process. includes dowloading extracting data
from textSummariser.logging import logger
#used to log messages, errors and other information


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()