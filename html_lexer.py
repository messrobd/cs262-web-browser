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
  ('javascript', 'exclusive')
)

t_ignore = ' ' # shorthand way of passing over all whitespace

# rules. order is important
# handling of comments: we will put the lexer into an explicit state, in which
# no html tokens will be generated. we'll just increment the line number
def t_htmlcomment(token): # not capitalised, because not a token value (?)
    r'<!--'
    token.lexer.begin('htmlcomment') # put lexer in 'htmlcomment' state

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.lineno += token.value.count('\n') # ensure count of lines includes those in comment
    token.lexer.begin('INITIAL') # return lexer to normal

def t_htmlcomment_error(token): # the charcters in the comment would result in errors without a rule
    token.lexer.skip(1) # skip gathers the text up so that it's available to count the newlines

# handling of javascript: similar to comments, except we eventually return the
# whole script as one token. we'll also increment the line number
def t_javascript(token):
    r'\<script\ type=\"text\/javascript\"\>'
    token.lexer.code_start = token.lexer.lexpos # store the index of the charactacter at which the js begins
    token.lexer.begin('javascript') # put lexer in 'javascript' state

def t_javascript_end(token):
    r'\<\/script\>'
    start_index, stop_index = token.lexer.code_start, token.lexer.lexpos - 9 # 9 ch in end tag
    token.value = token.lexer.lexdata[start_index: stop_index] # write all the data from the js lexer into one token
    token.type = 'JAVASCRIPT'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')
    return token

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
def hex_to_dec(string):
    hex_digits = string[2:]
    digit_lookup = '0123456789abcdef'
    decimal = 0
    exp = len(hex_digits)-1
    for h in hex_digits:
        decimal += digit_lookup.find(h)*16**exp
        exp -= 1
    return decimal

def t_NUMBER_hex(token): # from prob set 2
    r'0x[0-f]+'
    token.value = hex_to_dec(token.value)
    token.type = 'NUMBER' # needed because the definition isn't literal
    return token

def t_INTEGER(token):
    r'[0-9]+'
    token.value = int(token.value) # tranform token from string to number
    return token

def t_ID(token): # from prob set 2
    r'[a-zA-Z]+'
    return token

not used (yet) '''

def t_WORD(token):
    r'[^<> \n]+' # any number of characters except <, >, ' ' (space) and newline
    return token
