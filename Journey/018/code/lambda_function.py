#!/usr/bin/env python

import time
import boto3
import csv

table="Bookmarks-sync"

dynamo=boto3.client('dynamodb')

s3client = boto3.client('s3')

def get_file_s3(event):

    bucket = event['Records'][0]['s3']['bucket']['name']
    file = event['Records'][0]['s3']['object']['key']
    path = f"/tmp/{file}"

    s3client.download_file(
            Bucket=bucket,
            Key=file,
            Filename=path
            )

    return path

def lambda_handler(event, context):

    path=get_file_s3(event)

    with open(path,'r') as s3file:

        csv_reader = csv.reader(s3file, delimiter=",")

        for row in csv_reader:

            sno, url = row

            entry={
                  "SNo": {
                    "S": str(sno)
                  },
                  "DateAddedTS": {
                    "N": f"{round(time.time())}"
                  },
                  "Link": {
                    "S": url
                  }
                }
            dynamo.put_item(
                    TableName=table,
                    Item=entry
                    )

    return {
        "status" : 200
        }
