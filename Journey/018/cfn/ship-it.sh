#!/usr/bin/bash

# delete curently working stack
echo "Deleting nested stack to start afresh......"
aws cloudformation delete-stack --stack-name nested-dojo-stack

# upload latest nested cloudformation template files to s3 bucket
echo "Uploading latest nested template files to S3.........."
aws s3 cp nested-lambda.yaml s3://book-sync-source/nested-lambda.yaml
aws s3 cp nested-s3Bucket.yaml s3://book-sync-source/nested-s3Bucket.yaml
aws s3 cp nested-sns-topic.yaml s3://book-sync-source/nested-sns-topic.yaml
aws s3 cp nested-dynamodb.yaml s3://book-sync-source/nested-dynamodb.yaml

# Create Nested stack
echo "Creating Nested Stack......"
aws cloudformation create-stack --template-body file:///$(pwd)/cfn-root-stack.yaml --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --stack-name nested-dojo-stack
