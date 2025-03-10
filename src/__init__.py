import os
import json

def getPath(path):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', path)

def getKeyword():
    with open(getPath('keywords.json'), 'r') as f:
        return json.load(f)

def getOperator():
    operator_dir = getPath('operators')
    operator_dict = {}
    for filename in os.listdir(operator_dir):
        if filename.endswith('.json'):
            key = filename.replace('operator', '').replace('.json', '')
            with open(os.path.join(operator_dir, filename), 'r') as f:
                operator_dict[key.lower] = dict(json.load(f))
    return operator_dict


keywords = getKeyword()
operators = getOperator()