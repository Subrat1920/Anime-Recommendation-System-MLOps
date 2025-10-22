import os
import sys
from pathlib import Path
import pandas as pd
from src.logger.logger import logging
from src.exception.exception_handling import CustomException
import yaml

def read_yaml(file_path:Path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not the given path")
        with open(file_path, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logging.info("Succesfully read the YAML File")
            return config
    except Exception as e:
        logging.error("An [ERROR] while reading the YAML File")
        raise CustomException(e, sys)