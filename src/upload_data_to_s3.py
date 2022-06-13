import boto3


# Create an S3 access object
s3 = boto3.client("s3")


def upload_data(PATH: str, countryCode: str) -> str:
    s3.upload_file(
        Filename=f"{PATH}{countryCode}.csv",
        Bucket="nasdaq-data-bucket",
        Key=f"{PATH}{countryCode}.csv",
    )
    print(f"{countryCode}.csv uploaded successfully!")
