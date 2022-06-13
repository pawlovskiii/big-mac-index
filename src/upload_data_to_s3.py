import boto3


# Create an S3 access object
s3 = boto3.client("s3")


def upload_data_to_s3(PATH: str, countryCode: str) -> None:
    s3.upload_file(
        Filename=f"{PATH}{countryCode}.csv",
        Bucket="nasdaq-data-bucket",
        Key=f"{PATH}{countryCode}.csv",
    )
    print(f"{countryCode}.csv uploaded successfully!")
