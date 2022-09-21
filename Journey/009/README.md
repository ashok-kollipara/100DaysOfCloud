# Day-9 : Part-3 - Integration code completion and demo / testing

## Introduction

- Today's post is in continuation to the Thumbnail generator coding using SDK for architecture integration and demo of the working code to mark it ready for deployment

### Architecture

![Architecture](assets/Thumbnail-creator-crop.png)


## Prerequisite

- Understanding of python dictionaries and functions / loops, ability to use external libraries

- AWS services in use for this project - SNS, SQS, S3 and their functionalities to pick from SDK and integrate into the code

## Use Case

- Thumbnail generation for profile pictures, album arts for songs/music albums from input HD images

## Cloud Research

- Understanding the difference between SDK services
    - [Low-level client] (https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html)
    - [Resource](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html) 

- Difficulty in obtaining the required topic ARN for SNS with Topic Name
    - Currently implemented with picking from single entry of `list_topics` client method

- Used too much variables with pass by value instead of doing by OOPs way of pass by reference with hardcoded regions. 

- Studied today on Amazon Kinesis services

- Kickstarted Lambda Serverless compute

## Working Demo

![Demo](assets/sdk_demo.gif)

### Breakdown 1 — File in Source S3 bucket from CLI

![Source Bucket](assets/source-bucket-screen.png)

### Breakdown 2 — File in Destination Thumbnail S3 bucket

![Thumbnail Bucket](assets/thumbnail-bucket-screen.png)

### Breakdown 3 — Email with presigned URL arrives

![Email Arrives](assets/email-inbox-screen.png)

![Email Content](assets/email-content-screen.png)

## ☁️ Cloud Outcome

- Able to automate the Upload of image to S3 bucket, generate its thumbnail and uploading thumbnail to its own bucket in addition notifying end user with a preview link of thumbnail for confirmation

## Next Steps

- Make this work on AWS Lambda serverless and aim to minimize memory foot print for the code to run

## Social Proof

Will post on **Discord** channel - 100DaysofCloud
