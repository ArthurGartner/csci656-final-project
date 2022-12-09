import requests
import json

def lambda_handler(event, context):
    results = {}
    for eventval in event:
        try:
            response = requests.get(event[eventval])
            results[eventval] = response.status_code
        except:
            results[eventval] = 500
    json_response = json.dumps(results)
    return json_response
