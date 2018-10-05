from interpreter import *
'''
html_simple = [("word-elt","Hello")]
print interpret_html(html_simple)

html_body = [('tag-elt', 'body', [], [('tag-elt', 'b', [], [('word-elt', 'Hello World')], 'b')], 'body')]
print interpret_html(html_body)

html_negative = [('tag-elt', 'body', [], [('tag-elt', 'i', [], [('word-elt', 'Hello World')], 'b')], 'body')]
print interpret_html(html_negative)

test_tree1 = ("binop", ("number","5"),"+",("number","8"))
print eval_exp(test_tree1, (None, {})) # 13

test_tree2 = ("number", "1776")
print eval_exp(test_tree2, (None, {})) # 1776

test_tree3 = ("binop", ("number","5"),"+",("binop",("number","7"),"-",("number","18")))
print eval_exp(test_tree3, (None, {})) # -6

environment = (None, {"x" : 2})

tree = ("binop", ("identifier","x"), "+", ("number","2"))
print eval_exp(tree, environment) # 4.0

tree = ("if-then-else", ("true", "true"), [("assign", "x", ("number", "8"))], [("assign", "x", "5")])
eval_stmt(tree, environment)
print environment # (None, {"x" : 8.0})

sqrt = ("function",("x"),(("return",("binop",("identifier","x"),"*",("identifier","x"))),),{})
environment = (None, {"sqrt":sqrt})
print eval_exp(("call","sqrt",[("number","2")]), environment) # 4.0

script_var = """
var whatever = 0;
write(whatever); """
js_ast = js_parser.parse(script_var, lexer=js_lexer)
print js_ast
print interpret_js(js_ast)

script_func = """
function tricky(i) {
  if (i <= 0) {
    return i;
  } ;
  if ((i % 2) == 1) {
    write(i);
  } else {
    write(i);
  } ;
  return tricky(i - 1);
}
tricky(10); """
js_ast = js_parser.parse(script_func, lexer=js_lexer)
print js_ast
print interpret_js(js_ast)

webpage_tagargs = """<p id="whatever">This is my webpage! </p>"""
html_ast = html_parser.parse(webpage_tagargs, lexer=html_lexer)
print html_ast
interpret_html(html_ast)

webpage_anchor = """<a href='http://whatever.com'>This is my link! </a>"""
html_ast = html_parser.parse(webpage_anchor, lexer=html_lexer)
print html_ast
interpret_html(html_ast)

webpage_script_simple = """<html>
<h1>Simple script</h1>
<p>
This paragraph starts in HTML ...
<script type="text/javascript">write("This is my script!");
</script>
... and this paragraph finishes in HTML.
</p>
</html>"""
html_ast = html_parser.parse(webpage_script_simple, lexer=html_lexer)
#print html_ast
interpret_html(html_ast)

webpage = """<html>
<h1>JavaScript That Produces HTML</h1>
<p>
This paragraph starts in HTML ...
<script type="text/javascript">
write("<b>This whole sentence should be bold, and the concepts in this problem touch on the <a href='http://en.wikipedia.org/wiki/Document_Object_Model'>Document Object Model</a>, which allows web browsers and scripts to <i>manipulate</i> webpages.</b>");
</script>
... and this paragraph finishes in HTML.
</p>
<hr> </hr> <!-- draw a horizontal bar -->
<p>
Now we will use JavaScript to display even numbers in <i>italics</i> and
odd numbers in <b>bold</b>. <br> </br>
<script type="text/javascript">
function tricky(i) {
  if (i <= 0) {
    return i;
  } ;
  if ((i % 2) == 1) {
    write("<b>");
    write(i);
    write("</b>");
  } else {
    write("<i>");
    write(i);
    write("</i>");
  } ;
  return tricky(i - 1);
}
tricky(10);
</script>
</p>
</html>"""
html_ast = html_parser.parse(webpage, lexer=html_lexer)
#print html_ast
interpret_html(html_ast)

js_func_var = "var myfun = function() { return true ; }; write(myfun());"
js_ast = js_parser.parse(js_func_var, lexer=js_lexer)
print js_ast
print interpret_js(js_ast)
'''
js_func_closure = """
function makeGreeting(salutation) {
  var punc = "!";
  var greeting = function(person) {
    write(salutation);
    write(person + punc);
  };
  return greeting;
}
var greet = makeGreeting("ciao");
//greet("meg"); """
js_ast = js_parser.parse(js_func_closure, lexer=js_lexer)
print js_ast
print interpret_js(js_ast)
