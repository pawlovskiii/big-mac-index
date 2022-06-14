import requests
import boto3
from configparser import ConfigParser
from src.send_mail import post_mail
from src.extract_metadata import get_country_code
from src.local_storage import save_data_local
from src.upload_data_to_s3 import upload_data_to_s3


def main() -> None:
    config = ConfigParser()
    config.read("config.ini")

    API_KEY = config["DEFAULT"]["api_key"]
    PATH = config["DEFAULT"]["path"]
    BUCKET = config["DEFAULT"]["bucket"]

    HOST_CODE = config["DEFAULT"]["host_code"]
    SENDER = config["DEFAULT"]["sender"]
    RECEIVER = config["DEFAULT"]["receiver"]

    # Create an S3 access object
    s3 = boto3.client("s3")

    # Extract data from API
    for countryCode in get_country_code():
        response = requests.get(
            f"https://data.nasdaq.com/api/v3/datasets/ECONOMIST/{countryCode}.csv?api_key={API_KEY}"
        )
        save_data_local(PATH, response, countryCode)
        upload_data_to_s3(PATH, BUCKET, countryCode, s3)

    post_mail(HOST_CODE, SENDER, RECEIVER)


if __name__ == "__main__":
    main()
