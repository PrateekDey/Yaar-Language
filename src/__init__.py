import os
import json

def getPath(path):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', path)

def getKeyword():
    with open(getPath('keywords.json'), 'r') as f:
        return json.load(f)
    

keywords = getKeyword()