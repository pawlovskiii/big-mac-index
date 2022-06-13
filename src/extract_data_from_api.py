import requests
from configparser import ConfigParser
from src.extract_metadata import countryCodeList
from src.local_storage import save_data_local


config = ConfigParser()
config.read("config.ini")


def extract_data_from_api():
    for countryCode in countryCodeList[60:]:
        response = requests.get(
            f"https://data.nasdaq.com/api/v3/datasets/ECONOMIST/{countryCode}?api_key={config['DEFAULT']['api_key']}"
        )
        save_data_local(response, countryCode)
