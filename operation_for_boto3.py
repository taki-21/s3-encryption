# 参考:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object

import os
import uuid

import boto3
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(verbose=True, dotenv_path=dotenv_path)

SSE_CUSTOMER_KEY_BASE64 = os.environ.get("SSE_CUSTOMER_KEY_BASE64")
SSE_CUSTOMER_KEY_MD5 = os.environ.get("SSE_CUSTOMER_KEY_MD5")

PROFILE = os.environ.get("PROFILE")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
KEY = os.environ.get("KEY")
session = boto3.Session(profile_name=PROFILE)
client = session.client('s3')

response = client.get_object(
    Bucket=BUCKET_NAME,
    Key=KEY,
    SSECustomerAlgorithm='AES256',
    SSECustomerKey=SSE_CUSTOMER_KEY_BASE64,
    SSECustomerKeyMD5=SSE_CUSTOMER_KEY_MD5
)

print('response: ', response)

binary = response['Body'].read()


# 画像を保存
img_path = 'tmp/' + str(uuid.uuid4()) + '.jpg'
with open(img_path, "wb") as f:
    f.write(binary)
