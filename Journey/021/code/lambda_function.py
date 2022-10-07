#!/usr/bin/env python

import time

def lambda_handler(event, context):
    
    val = int(time.strftime('%H'))
    action = 'Work'

    if val > 23:
        action = 'Sleeep'
    else:
        action = 'RockIt'

    return {
        "action" : action
        }
