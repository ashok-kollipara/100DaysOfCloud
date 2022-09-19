# Day-8 : Part-2 - Python Boto3 SDK - Scripting for Architecture Integration

## Introduction

- I did some scripting today and done halfway with study and application of Boto3 SDK for AWS using Python

## Use Case

- Idea is to receive the SQS message body to extract file name from S3 event for uploaded HD file 
- Download HD image from Source S3 bucket and resize it as thumbnail using python PIL - pillow image library
- Delete the SQS message after processing if its done within visiblity timeout

## Cloud Research

- [Python Boto3 SDK documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

- Also studied about SQS FIFO Queues and SNS for further refinement and Integration
    - De-deduplication ID
    - SequenceNumber
    - SNS-SQS Fanout

## Code - EOD Today 

### Half done - after prototyping will do conversion to OOPS / asyncio

```python

#!/usr/bin/env python

import json
import boto3
from PIL import Image


def get_queue(sourceQ):

    # Set the service client and resource
    q_client = boto3.client('sqs',region_name=region)

    # Get the queue url
    q_url_response = q_client.get_queue_url(QueueName=sourceQ)
    q_url = q_url_response['QueueUrl']

    print(f'QueueURL = {q_url}')

    return q_url

def image_reduction(s_bucket, t_bucket, sourcefile):

    local_file = "/tmp/" + sourcefile
    thumbnail_image = "thumbnail" + "_" + sourcefile

    # download file from source bucket
    s_bucket.download_file(sourcefile,local_file)

    # reduce image size in place - using thumbnail function 
    # instead of resize function
    try:
        img = Image.open(local_file)
        img.thumbnail(thumb_size)
        img.save(thumbnail_image)

        # Upload to thumbnail bucket
        t_bucket.upload_file(
                Key=thumbnail_image,
                Filename=thumbnail_image
                )
    except:
        raise ExceptionError as 'Failed Image processing or upload'

def process_queue(q_url, s_bucket, t_bucket, sourcefile):

    '''
    Reference the client or use session based client for this operation ?
    '''

    msg_response = q_client.receive_message(
        QueueUrl=q_url,
        MaxNumberOfMessages=5,
        VisibilityTimeout=30,
        WaitTimeSeconds=15
    )

    try:
        print(f"Received {len(msg_response['Messages'])} messages")

        for message in msg_response['Messages']:

            s3_object_name = message['Body']
            msg_rhandle = message['ReceiptHandle']

            print('Processing message completed.....Deleting message from queue')

            image_reduction(s_bucket, t_bucket, s3_object_name)

            del_response = q_client.delete_message(
                    QueueUrl = q_url,
                    ReceiptHandle = message['ReceiptHandle'],
                    )

            print(json.dumps(del_response,indent=4))

    except Keyerror:
        
        ''' No messages in Queue..Poll again or check Dead Letter Queue list '''
        # print(json.dumps(msg_response,indent=4))

if __name__ == '__main__':

    region='us-east-1'
    sourceQ='practiceQ'
    source_bucket='naa-hd-image-source'
    thumb_bucket='naa-thumb-bucket'
    thumb_size=(64,64)

    # setup s3 resource
    s3 = boto3.resource('s3')

    # map source bucket resources
    s_bucket = s3.Bucket(source_bucket)
    t_bukcet = s3.Bucket(thumb_bucket)

    # start process

    q_url = get_queue(sourceQ)

    process_queue(q_url)
```

## Social Proof

Will post on **Discord** channel
