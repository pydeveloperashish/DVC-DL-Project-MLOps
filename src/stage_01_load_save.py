from src.utils.all_utils import create_directory, read_yaml, copy_file
import argparse
import os
import pandas as pd
from pprint import pprint
import shutil
from tqdm import tqdm

        
        
def get_data(config_path):
    config = read_yaml(config_path)
    source_download_dirs = config["source_download_dirs"]
    local_data_dirs = config["local_data_dirs"]
    
    for source_download_dir, local_data_dir in tqdm(zip(source_download_dirs, local_data_dirs), total = 2, desc = "List of Folders", colour = 'red'):
        create_directory([local_data_dirs])
        copy_file(source_download_dir, local_data_dir)
        

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default = "config/config.yaml")
    parsed_args = args.parse_args()
    get_data(config_path = parsed_args.config)
     
    