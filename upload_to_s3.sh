#!/bin/bash

# ./.envファイルを読み込んで変数として参照できるようにする
source ./.env

aws s3api put-object \
  --bucket $BUCKET_NAME \
  --key $KEY \
  --body $KEY \
  --sse-customer-algorithm AES256 \
  --sse-customer-key $SSE_CUSTOMER_KEY_BASE64 \
  --sse-customer-key-md5 $SSE_CUSTOMER_KEY_MD5 \
  --profile $PROFILE
