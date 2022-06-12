from os import listdir
import boto3


def find_csv_filenames(path_to_dir):
    return listdir(path_to_dir)


folderData = find_csv_filenames("bigmac_index")

# Create an S3 access object
s3 = boto3.client("s3")


def upload_data():
    for file in folderData:
        s3.upload_file(Filename=f"bigmac_index/{file}", Bucket="nasdaq-data-bucket", Key=f"bigmac_index/{file}")
        print(f"{file} uploaded successfully!")
