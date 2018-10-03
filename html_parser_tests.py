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
print test_lexer(webpage)
print test_parser(webpage)

webpage_tagargs = '''<p id="whatever">This is my webpage! </p>'''
print test_lexer(webpage_tagargs)
print test_parser(webpage_tagargs)

webpage_anchor = '''<a href='http://whatever.com'>This is my link! </a>'''
print test_lexer(webpage_anchor)
print test_parser(webpage_anchor)

webpage_script_simple = """<html>
<h1>Simple script</h1>
<p>
This paragraph starts in HTML ...
<script type="text/javascript">write("SCRIPT OUTPUT");
</script>
... and this paragraph finishes in HTML.
</p>
</html>"""
print test_lexer(webpage_script_simple)
