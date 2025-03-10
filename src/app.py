from . import lexer

input = '''
    iss a mai 10;
    iss b mai 20;
    iss c mai a plus b;
    dikhao c;
    '''

tokens = lexer.mindMap(input)

print(tokens)