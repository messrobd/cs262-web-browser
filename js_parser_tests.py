import ply.lex as lex
import ply.yacc as yacc
import js_lexer
import js_parser

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
parser = yacc.yacc(module=js_parser)
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
'''
js_simple_exp = 'sum = 1 + 2;'
#print test_lexer(js_simple_exp)
print test_parser(js_simple_exp)

js_simple_declare = 'var string = "whatever";'
#print test_lexer(js_simple_declare)
print test_parser(js_simple_declare)

js_simple_associativity = '1 - 2 - 3;'
print test_parser(js_simple_associativity)

js_asso_precedence = '1 + 2 * 3 - 4 / 5 * (6 + 2);'
print test_parser(js_asso_precedence)

js_string_bool = '"hello" == "goodbye" || true && false;'
print test_parser(js_string_bool)

js_not = '! ! tricky || 3 < 5;'
print test_parser(js_not)

js_nested_calls = 'apply(1, 2 + eval(recursion), sqrt(2));'
print test_parser(js_nested_calls)
