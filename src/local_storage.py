import json
import pandas as pd
from requests import Response
from src.upload_data_to_s3 import upload_data


def save_data_local(PATH: str, response: Response, countryCode: str) -> None:
    data = json.dumps(response.json())
    read_data = pd.read_json(data)
    read_data.to_csv(rf"{PATH}{countryCode}.csv", index=False)
    print(f"{countryCode} saved successfully!")
    upload_data(PATH, countryCode)
