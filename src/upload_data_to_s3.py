import pandas as pd
import requests
import json
import boto3
from src.extract_metadata import countryCodeList


# Create an S3 access object
s3 = boto3.client("s3")


def upload_data(countryCode):
    s3.upload_file(
        Filename=f"bigmac_index/{countryCode}.csv",
        Bucket="nasdaq-data-bucket",
        Key=f"bigmac_index/{countryCode}.csv",
    )
    print(f"{countryCode}.csv uploaded successfully!")


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
