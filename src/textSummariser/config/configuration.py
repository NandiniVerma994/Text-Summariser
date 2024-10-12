from textSummariser.constants import *
from textSummariser.utils.common import read_yaml, create_directories
from textSummariser.entity import (DataIngestionConfig, DataValidationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        #read both the files and return the contents of the file
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        #create directorie using config because it is box type output
        create_directories([self.config.artifacts_root])
        #it will create data ingestion folder. inside that data ingestion where it will be downloading the data
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        #creating root directory  and then performing all the below things like unzipping the data
        create_directories([config.root_dir])
        #here DataIngestionConfig is the return type as already mentioned in config.yaml
        data_ingestion_config = DataIngestionConfig(
            #below are the things it wil return
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    #also import data validation config
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config