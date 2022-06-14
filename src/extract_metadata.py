from typing import List
import pandas as pd


def get_country_code() -> List[str]:
    metadata = pd.read_csv(r"ECONOMIST_metadata.csv")
    countryCodeList = metadata["code"].tolist()
    return countryCodeList
