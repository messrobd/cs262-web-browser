import ply.lex as lex
from js_lexer import lexer

def test_lexer(input_string): #copied this useful func from exercise
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type, tok.value]
  return result

tokens = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

print test_lexer(tokens)

comments = """
if // else mystery
=/*=*/=
true /* false
*/ return"""

print test_lexer(comments)

input1 = 'some_identifier -12.34 "a \\"escape\\" b"'
print test_lexer(input1)


input2 = '-12x34'
print test_lexer(input2)
