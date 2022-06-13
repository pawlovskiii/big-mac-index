from botocore.client import BaseClient


def upload_data_to_s3(PATH: str, BUCKET: str, countryCode: str, s3: BaseClient) -> None:
    s3.upload_file(
        Filename=f"{PATH}{countryCode}.csv",
        Bucket=BUCKET,
        Key=f"{PATH}{countryCode}.csv",
    )
    print(f"{countryCode}.csv uploaded successfully!")
