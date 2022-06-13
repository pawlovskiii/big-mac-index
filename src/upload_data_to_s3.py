import boto3


# Create an S3 access object
s3 = boto3.client("s3")


def upload_data(config, countryCode: str) -> str:
    s3.upload_file(
        Filename=f"{config['DEFAULT']['path']}{countryCode}.csv",
        Bucket="nasdaq-data-bucket",
        Key=f"{config['DEFAULT']['path']}{countryCode}.csv",
    )
    print(f"{countryCode}.csv uploaded successfully!")
