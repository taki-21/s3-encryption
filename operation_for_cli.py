import os
import subprocess
import uuid

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(verbose=True, dotenv_path=dotenv_path)

SSE_CUSTOMER_KEY_BASE64 = os.environ.get("SSE_CUSTOMER_KEY_BASE64")
SSE_CUSTOMER_KEY_MD5 = os.environ.get("SSE_CUSTOMER_KEY_MD5")
PROFILE = os.environ.get("PROFILE")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
KEY = os.environ.get("KEY")

img_path = 'tmp/' + str(uuid.uuid4()) + '.jpg'


response = subprocess.call(['aws', 's3api',
                            'get-object', img_path,
                            '--bucket', BUCKET_NAME,
                            '--key', KEY,
                            '--sse-customer-algorithm', 'AES256',
                            '--sse-customer-key', SSE_CUSTOMER_KEY_BASE64,
                            '--sse-customer-key-md5', SSE_CUSTOMER_KEY_MD5,
                            '--profile', PROFILE])

print('response: ', response)
