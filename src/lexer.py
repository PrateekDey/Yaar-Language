import re
from . import keywords, operators

def tokenizer(input):
    lines = input.split('\n')
    tokens = [cleaned_line.split() for cleaned_line in [line.strip().replace(';','') for line in lines] if cleaned_line != '']
    return tokens

def mindMap(input):
    tokens = tokenizer(input)
    keyword_set = set(keywords.keys())
    operator_set = {op for sub_dict in operators.values() for op in sub_dict.keys()}
    
    for line in tokens:
        for token in line:
            if token.isdigit():
                print(token, " is a number")
            elif token in keyword_set:
                print(token, " is a keyword")
            elif token in operator_set:
                print(token, " is an operator")
            else:
                print(token, " is a Variable")