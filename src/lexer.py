import os
import re
import json

class Tokenizer:
    def getCleanedInput(self, input) -> str:
        return re.sub(r'[^\w\s_]', ' ', input)

    def getLines(self, input) -> list:
        return input.split('\n')

    def getWords(self, line) -> list:
        return line.strip().split(' ')

    def getTokens(self, input) -> list:
        return [self.getWords(line) for line in self.getLines(self.getCleanedInput(input)) if line]


class Parser:
    def __init__(self):
        self.keywords = self.getKeywords()
        self.operators = self.getOperators()

    def getPath(self, path) -> str:
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', path)
    
    def getKeywords(self):
        with open(self.getPath('keywords.json'), 'r') as f:
            return json.load(f)
        
    def getOperators(self):
        with open(self.getPath('operators.json'), 'r') as f:
            return json.load(f)

    def getParsedTokens(self, tokens: list[list[str]]) -> list[dict]:
        keys_keywords = self.keywords.keys()
        keys_operators = self.operators.keys()
        ast = list()

        for line in tokens:
            for element in line:
                if element.isdigit():
                    ast.append({'type': 'number', 'value': element})
                elif element in keys_keywords:
                    ast.append({'type': 'keyword', 'token': element, 'value': self.keywords[element]})
                elif element in keys_operators:
                    ast.append({'type': 'operator', 'token': element, 'value': self.operators[element]})
                else:
                    ast.append({'type': 'identifier', 'token': element})

        return ast