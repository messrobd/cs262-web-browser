import ply.lex as lex
import ply.yacc as yacc
import js_lexer
from js_lexer import tokens
from  js_parser import *

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

lexer = lex.lex(module=js_lexer)
parser = yacc.yacc()
'''
test_tokens = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """
print test_lexer(test_tokens)

comments = """
if // else mystery
=/*=*/=
true /* false
*/ return"""
print test_lexer(comments)

false_prophets = 'false_prophets "false_prophets true prophets"'
print test_lexer(false_prophets)

input1 = 'some_identifier -12.34 "a \\"escape\\" b"'
print test_lexer(input1)

input2 = '-12x34'
print test_lexer(input2)
'''
js_simple_stmt = 'var president = trump;'
#print test_lexer(js_simple_stmt)
print test_parser(js_simple_stmt)

js_simple_func = "function myfun() { return nothing ; }"
#print test_lexer(js_simple_func)
print test_parser(js_simple_func)

js_func_args = "function nobletruths(dukkha,samudaya,nirodha,gamini) { return buddhism ; }"
print test_parser(js_func_args)

js_multi_top ="""var view = right;
var intention = right;
var speech = right;
action = right;
livelihood = right;
effort_right;
mindfulness_right;
concentration_right;"""
print test_parser(js_multi_top)

js_if_else = """
if cherry {
  orchard;
  if uncle_vanya {
    anton ;
    chekov ;
  } else {
  } ;
  nineteen_oh_four ;
} ;
"""
print test_parser(js_if_else)
