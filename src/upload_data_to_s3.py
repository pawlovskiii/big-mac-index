import boto3

# Create an S3 access object
s3 = boto3.client("s3")


def upload_data(countryCode):
    s3.upload_file(
        Filename=f"bigmac_index/{countryCode}.csv",
        Bucket="nasdaq-data-bucket",
        Key=f"bigmac_index/{countryCode}.csv",
    )
    print(f"{countryCode}.csv uploaded successfully!")
