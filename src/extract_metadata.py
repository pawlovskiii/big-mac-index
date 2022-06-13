import pandas as pd

metadata = pd.read_csv(r"ECONOMIST_metadata.csv")
countryCodeList = metadata["code"].tolist()
