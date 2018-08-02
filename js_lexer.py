'''
comments & keywords (lesson 7: prob set 2, #3)

define token definition rules for all tokens in the JS subset except IDENTIFIER,
NUMBER and STRING

also handle // eol comments and /* */ multiline comments '''

import ply.lex as lex
import re

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
)

states = (
        ('jscomment', 'exclusive'),
)

t_ignore = ' \t\v\r' # whitespace

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
    r'('
    return token

def t_RPAREN(token):
    r')'
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
