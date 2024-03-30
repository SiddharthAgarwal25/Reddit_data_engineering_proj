import s3fs
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY

def connection_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False, key=AWS_ACCESS_KEY_ID, secret=AWS_ACCESS_KEY)
        print("connection established with AWS")
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exist(S3:s3fs.S3FileSystem, bucket:str):
    try:
        print(f"searching for .. {bucket}")
        if not S3.exists(bucket):
            print("Bucket does not exist, creating bucket...")
            S3.mkdir(bucket)
            print("Bucket created...")
        else:
            print("Bucket already exists")
    except Exception as e:
        print(e)


def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket:str, s3_file_name: str):
    try:
        s3.put(file_path, bucket+'/raw/'+ s3_file_name)
        print(f'File uploaded to {bucket}')
    except FileNotFoundError:
        print('The file was not found')