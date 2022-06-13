import json
import pandas as pd
from src.upload_data_to_s3 import upload_data
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


def save_data_local(response, countryCode):
    data = json.dumps(response.json())
    read_data = pd.read_json(data)
    read_data.to_csv(rf"{config['DEFAULT']['path']}{countryCode}.csv", index=False)
    print(f"{countryCode} saved successfully!")
    upload_data(countryCode)
