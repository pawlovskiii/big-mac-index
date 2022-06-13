import requests
from src.extract_metadata import get_country_code
from src.local_storage import save_data_local


def extract_data_from_api(API_KEY: str, PATH: str) -> None:
    for countryCode in get_country_code():
        response = requests.get(
            f"https://data.nasdaq.com/api/v3/datasets/ECONOMIST/{countryCode}?api_key={API_KEY}"
        )
        save_data_local(PATH, response, countryCode)
