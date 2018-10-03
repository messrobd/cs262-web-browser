import ply.lex as lex
import ply.yacc as yacc
import html_lexer
import html_parser

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
    parse_tree = parser.parse(input_string, lexer=lexer)
    return parse_tree

lexer = lex.lex(module=html_lexer)
parser = yacc.yacc(module=html_parser)

webpage = '''This is <b>my</b> <!--bastard-->
          webpage!'''

webpage_tagargs = '''<p id="whatever">This is my webpage! </p>'''

print test_lexer(webpage)
print test_parser(webpage)

print test_lexer(webpage_tagargs)
print test_parser(webpage_tagargs)
