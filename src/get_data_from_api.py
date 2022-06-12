import pandas as pd
import requests
import json
import boto3


metadata = pd.read_csv(r"../ECONOMIST_metadata.csv")
countryCodeList = metadata["code"].tolist()

# Create an S3 access object
s3 = boto3.client("s3")


def json_to_csv(data, countryCode):
    read_data = pd.read_json(data)
    read_data.to_csv(rf"../bigmac_index/{countryCode}.csv", index=False)
    print(f"{countryCode} saved successfully!")
    s3.upload_file(
        Filename=f"../bigmac_index/{countryCode}.csv",
        Bucket="nasdaq-data-bucket",
        Key=f"bigmac_index/{countryCode}.csv",
    )
    print(f"{countryCode}.csv uploaded successfully!")


def get_data():
    for countryCode in countryCodeList[60:]:
        response = requests.get(
            f"https://data.nasdaq.com/api/v3/datasets/ECONOMIST/{countryCode}?api_key=Hy29GkkAwX2gVmj1wpLh"
        )
        data = json.dumps(response.json())
        json_to_csv(data, countryCode)
