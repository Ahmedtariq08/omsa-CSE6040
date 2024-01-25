import json


def printJson(dict):
    json_object = json.dumps(dict, indent=4)
    print(json_object)
