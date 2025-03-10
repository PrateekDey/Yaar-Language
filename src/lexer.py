from nltk.tokenize import word_tokenize
import os
import json

class Lexer:
    def __init__(self):
        getPath = lambda path: os.path.join(os.path.dirname(__file__), path)