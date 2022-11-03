#!/bin/bash

# ./.envファイルを読み込んで変数として参照できるようにする
source ./.env

UUID=`uuidgen`
echo $UUID
IMG_PATH="tmp/${UUID}.jpg"
echo $IMG_PATH

aws s3api get-object $IMG_PATH \
  --bucket ssec-sample \
  --key sample.jpg \
  --sse-customer-algorithm AES256 \
  --sse-customer-key $SSE_CUSTOMER_KEY_BASE64 \
  --sse-customer-key-md5 $SSE_CUSTOMER_KEY_MD5 \
  --profile $PROFILE
