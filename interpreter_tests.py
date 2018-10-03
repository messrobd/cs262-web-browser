from interpreter import *

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
