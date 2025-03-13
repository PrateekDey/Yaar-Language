from . import lexer

def yaar_started(filename):
    try:
        with open(filename, 'r') as file:
            input_string = file.read()
        token_lexer = lexer.Tokenizer()
        parser_lexer = lexer.Parser()
        tokens = token_lexer.getTokens(input_string)
        parsed_tokens = parser_lexer.getParsedTokens(tokens)
        print(parsed_tokens)
    except FileNotFoundError:
        print(f"File {filename} not found.")