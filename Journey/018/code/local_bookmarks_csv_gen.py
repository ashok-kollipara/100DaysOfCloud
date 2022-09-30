import sqlite3
import time
import boto3

def process_bookmarks(db_connection):

    command="SELECT url,description FROM MOZ_PLACES"

    val = db_connection.execute(command)

    with open('file.csv', 'w') as f:

        for count, row in enumerate(val,start=1):

            url, description = row

            print(count, url)

            f.write(f"{count},{url}\n")

    db_connection.commit()

    db_connection.close()

if __name__ == '__main__':

    path="places.sqlite"

    db_connection = sqlite3.connect(path)

    process_bookmarks(db_connection)
