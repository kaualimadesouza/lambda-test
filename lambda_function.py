import json
from log import log

def lambda_handler(event, context):
    log("Lambda function started with GH")

    nome = event.get("key1")
    return {
        'statusCode': 200,
        'body': event,
    }
