import ply.lex as lex
from js_lexer import lexer

def test_lexer(input_string): #copied this useful func from exercise
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
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
