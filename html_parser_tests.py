import ply.lex as lex
import ply.yacc as yacc
import html_lexer
from  html_parser import *

'''
test procedures (copied from tutorial): '''

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type, tok.value]
  return result

def test_parser(input_string):
    lexer.input(input_string)
    parse_tree = parser.parse(input_string,lexer=lexer)
    return parse_tree

lexer = lex.lex(module=html_lexer)
#parser = yacc.yacc()

webpage = '''This is <b>my</b> <!--bastard-->
          webpage!'''

print test_lexer(webpage)
