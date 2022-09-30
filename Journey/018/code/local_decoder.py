#!/usr/bin/env python

import csv

with open('file.csv','r') as f:

    csv_reader = csv.reader(f, delimiter=",")

    for row in csv_reader:

        sno, url = row
        print(sno, url)
