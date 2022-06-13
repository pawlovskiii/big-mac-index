import pandas as pd
import requests
import json
from src.extract_metadata import countryCodeList
from src.upload_data import upload_data


def json_to_csv(response, countryCode):
    data = json.dumps(response.json())
    read_data = pd.read_json(data)
    read_data.to_csv(rf"bigmac_index/{countryCode}.csv", index=False)
    print(f"{countryCode} saved successfully!")
    upload_data(countryCode)


def extract_data_from_api():
    for countryCode in countryCodeList[60:]:
        response = requests.get(
            f"https://data.nasdaq.com/api/v3/datasets/ECONOMIST/{countryCode}?api_key=Hy29GkkAwX2gVmj1wpLh"
        )
        json_to_csv(response, countryCode)

def main():
    extract_data_from_api()


if __name__ == "__main__":
    main()
