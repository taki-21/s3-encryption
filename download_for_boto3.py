import os
import uuid

import boto3
from dotenv import load_dotenv

# .envファイルの内容を読み込む
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(verbose=True, dotenv_path=dotenv_path)

# 環境変数を取得
BUCKET_NAME = os.environ.get("BUCKET_NAME")
KEY = os.environ.get("KEY")
SSE_CUSTOMER_KEY_BASE64 = os.environ.get("SSE_CUSTOMER_KEY_BASE64")
SSE_CUSTOMER_KEY_MD5 = os.environ.get("SSE_CUSTOMER_KEY_MD5")
PROFILE = os.environ.get("PROFILE")

# clientの作成
session = boto3.Session(profile_name=PROFILE)
client = session.client('s3')

# s3バケットからオブジェクトを取得する
response = client.get_object(
    Bucket=BUCKET_NAME,
    Key=KEY,
    SSECustomerAlgorithm='AES256',
    SSECustomerKey=SSE_CUSTOMER_KEY_BASE64,
    SSECustomerKeyMD5=SSE_CUSTOMER_KEY_MD5
)

print(response)

# レスポンスの中身を読み込む
binary = response['Body'].read()

# 画像を保存
img_path = 'tmp/' + str(uuid.uuid4()) + '.jpg'
with open(img_path, "wb") as f:
    f.write(binary)
