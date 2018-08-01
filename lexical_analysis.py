import ply.lex as lex # import the _lex_ lexer generator, I think

tokens = (
  'LANGLE', # order does not matter at this point
  'LANGLESLASH',
  'RANGLE',
  'EQUAL',
  'STRING',
  'WORD'
)
states = (
  ('htmlcomment','exclusive'), # once entered, no other rules will be considered
)

t_ignore = ' ' # shorthand way of passing over all whitespace

# rules. order is important
def t_htmlcomment(token): # not capitalised, because not a token value (?)
    r'<!--'
    token.lexer.begin('htmlcomment') # put lexer in htmlcomment state

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.lineno += token.value.count('\n') # ensure count of lines includes those in comment
    token.lexer.begin('INITIAL') # return lexer to normal

def t_htmlcomment_error(token): # the charcters in the comment would result in errors without a rule
    token.lexer.skip(1) # skip gathers the text up so that it's available to count the newlines

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1 # increment the line number property in the lexer
    pass # but we don't want the token in the results

def t_LANGLESLASH(token): # needs to preceed LANGLE
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

'''
def t_WHITESPACE(token): # needs to preceed string, or it might interfere with the body of the string
    r' '
    pass

not needed: replaced with t_ignore statement '''

def t_STRING(token):
    r'"[^"]*"' # match closing quotes only
    token.value = token.value[1:-1] # trim the enclosing quotes from the token
    return token

'''
def t_INTEGER(token):
    r'[0-9]+'
    token.value = int(token.value) # tranform token from string to number
    return token

def t_NUMBER(token):
    r'-?[0-9]+\.?[0-9]*'
    token.value = float(token.value)
    return token

def t_IDENTIFIER(token):
    r'[a-zA-Z][a-zA-Z_]*'
    return token

not used (yet) '''

def t_WORD(token):
    r'[^<> \n]+' # any number of characters except <, >, ' ' (space) and newline
    return token

# generate the lexer
htmllexer = lex.lex() # calls the lexer generator to instantiate a lexer

#call the lexer
webpage = '''This is <b>my</b> <!--bastard-->
          webpage!'''
htmllexer.input(webpage) # lex the webpage

while True:
    tok = htmllexer.token() # get the next token; I guess it's iterable
    if not tok: break
    print tok
