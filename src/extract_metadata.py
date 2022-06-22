from typing import List
import pandas as pd


def get_country_code() -> List[str]:
    metadata: pd.DataFrame = pd.read_csv(r"./metadata/ECONOMIST_metadata.csv")
    countryCodeList: List[str] = metadata["code"].tolist()
    return countryCodeList
