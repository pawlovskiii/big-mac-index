import csv
import json
import pandas as pd
from requests import Response


def save_data_local(PATH: str, response: Response, countryCode: str) -> None:
    url_content = response.content

    csv_file = open(f"{PATH}{countryCode}.csv", "wb")
    csv_file.write(url_content)
    csv_file.close()

    print(f"{countryCode} saved successfully!")
