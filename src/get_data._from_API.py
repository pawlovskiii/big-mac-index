import pandas as pd
import requests
import json


metadata = pd.read_csv(r"ECONOMIST_metadata.csv")
countryCodeList = metadata["code"].tolist()


def json_to_csv(data, countryCode):
    read_data = pd.read_json(data)
    read_data.to_csv(rf"bigmac_index/{countryCode}.csv", index=False)


for countryCode in countryCodeList: 
    response = requests.get(f"https://data.nasdaq.com/api/v3/datasets/ECONOMIST/{countryCode}?api_key=Hy29GkkAwX2gVmj1wpLh")
    data = json.dumps(response.json())
    json_to_csv(data, countryCode)
    print(f"{countryCode} saved successfully!")
