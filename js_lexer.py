'''
comments & keywords (lesson 7: prob set 2, #3)

define token definition rules for all tokens in the JS subset except IDENTIFIER,
NUMBER and STRING

also handle // eol comments and /* */ multiline comments '''

import ply.lex as lex

tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'MODULO',       # %
        'NOT',          # !
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
        'IDENTIFIER',
        'NUMBER',
        'STRING',
)

states = (
        ('jscomment', 'exclusive'),
)

t_ignore = ' \t\v\r' # whitespace
t_jscomment_ignore = ' \t\v\r' # whitespace

def t_error(token):
    token.lexer.skip(1)

def t_eol_comment(token):
    r'//[^\n]*'
    pass

def t_jscomment(token):
    r'/\*'
    token.lexer.begin('jscomment')

def t_jscomment_end(token):
    r'\*/'
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')

def t_jscomment_error(token):
    token.lexer.skip(1)

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_NUMBER(token):
    r'-?[0-9]+\.?[0-9]*'
    token.value = float(token.value)
    return token

def t_VAR(token):
    r'var'
    return token

def t_FUNCTION(token):
    r'function'
    return token

def t_IF(token):
    r'if'
    return token

def t_ELSE(token):
    r'else'
    return token

def t_RETURN(token):
    r'return'
    return token

def t_LPAREN(token):
    r'\('
    return token

def t_RPAREN(token):
    r'\)'
    return token

def t_LBRACE(token):
    r'{'
    return token

def t_RBRACE(token):
    r'}'
    return token

def t_COMMA(token):
    r','
    return token

def t_SEMICOLON(token):
    r';'
    return token

def t_NOT(token):
    r'!'
    return token

def t_ANDAND(token):
    r'&&'
    return token

def t_OROR(token):
    r'\|\|'
    return token

def t_EQUALEQUAL(token):
    r'=='
    return token

def t_GE(token):
    r'>='
    return token

def t_LE(token):
    r'<='
    return token

def t_GT(token):
    r'>'
    return token

def t_LT(token):
    r'<'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_PLUS(token):
    r'\+'
    return token

def t_MINUS(token):
    r'\-'
    return token

def t_MODULO(token):
    r'\%'
    return token

def t_TIMES(token):
    r'\*'
    return token

def t_DIVIDE(token):
    r'/'
    return token

def t_TRUE(token):
    r'true'
    return token

def t_FALSE(token):
    r'false'
    return token

def t_IDENTIFIER(token):
    r'[a-zA-Z][a-zA-Z_]*'
    return token

def t_STRING(token):
    r'"(?:[^"\\]|(?:\\.))*"'
    token.value = token.value[1:-1]
    return token

'''
numbers and strings (lesson 7: prob set 2, #4)

add token definitions for numbers, identifiers (names of variables and
functions) and strings. definitions:
  * identifier must start with an upper or lowercase ch. it can then contain any
  number of upper or lowercase ch's, with or without underscores
  * number is one or more digits and may start with a - Return value miust be a
  float
  * string is zero or more ch contained in double quotes. a string may contain
  escaped characters, eg \" does not end a string. return the string minus
  enclosing quotes

remember: to get python to evaluate an escape character you have to unescape it
  * test "a \"escape\" b" ==> "a \\"escape\\" b" to test correctly

definitions had to be spliced into list to get the rules right '''
