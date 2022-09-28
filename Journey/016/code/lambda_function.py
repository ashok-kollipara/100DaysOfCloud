#!/usr/bin/env python

import json

def lambda_handler(event, context):

    print ("Hello Dude")

    return {
        "status" : 200
        }
