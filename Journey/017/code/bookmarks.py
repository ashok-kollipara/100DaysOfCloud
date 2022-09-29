import sqlite3
import time
import boto3

def get_file_s3(s3client):

    '''
    bucket = event['Records'][0]['s3']['bucket']['name']
    file = event['Records'][0]['s3']['object']['key']
    '''

    bucket="naa-sontha-bucket"
    file="page.html"

    s3client.download_file(
            Bucket=bucket,
            Key=file,
            Filename=f"/tmp/{file}"
            )

def process_bookmarks(db_connection, dynamo, path, table):

    command="SELECT url,description FROM MOZ_PLACES"

    val = db_connection.execute(command)

    for count, row in enumerate(val,start=1):

        url, description = row

        print(count, url)

        entry={
              "SNo": {
                "S": str(count)
              },
              "DateAddedTS": {
                "N": f"{round(time.time())}"
              },
              "Description": {
                "S": f"{description}"
              },
              "Link": {
                "S": url
              }
            }
        dynamo.put_item(
                TableName=table,
                Item=entry
                )

    db_connection.commit()

    db_connection.close()

if __name__ == '__main__':

    path="places.sqlite"

    table="Bookmarks-sync"

    db_connection = sqlite3.connect(path)

    dynamo=boto3.client('dynamodb')

    s3client = boto3.client('s3')

    get_file_s3(s3client)

    #process_bookmarks(db_connection, dynamo, path, table)
