import json
import pandas as pd
import requests
from src.upload_data_to_s3 import upload_data


Response = requests.models.Response


def save_data_local(PATH, response: Response, countryCode: str) -> str:
    data = json.dumps(response.json())
    read_data = pd.read_json(data)
    read_data.to_csv(rf"{PATH}{countryCode}.csv", index=False)
    print(f"{countryCode} saved successfully!")
    upload_data(PATH, countryCode)
