import ply.lex as lex
import ply.yacc as yacc
import js_lexer
import js_parser
import html_lexer
import html_parser

js_lexer = lex.lex(module=js_lexer)
js_parser = yacc.yacc(module=js_parser)
html_lexer = lex.lex(module=html_lexer)
html_parser = yacc.yacc(module=html_parser)

'''
procedure evaluates an expression (1 + 2, x + y). variable values are sought in
the current environment frame, then recursively up to global '''

def eval_exp(tree, environment):
    exptype = tree[0]
    if exptype == "number":
        return float(tree[1])
    elif exptype == "string":
        return tree[1]
    elif exptype == "true":
        return True
    elif exptype == "false":
        return False
    elif exptype == "not":
        return not(eval_exp(tree[1], environment))
    elif exptype == "binop":
        (left_child, operator, right_child) = tree[1:]
        x = eval_exp(left_child, environment)
        y = eval_exp(right_child, environment)
        return perform_binop(x, operator, y)
    elif exptype == "identifier":
        vname = tree[1]
        value = env_lookup(vname, environment)
        if value == None:
            print "ERROR: unbound variable " + vname
        else:
            return value
    elif exptype == "call":
        (fname, fargs) = tree[1:]
        fvalue = env_lookup(fname, environment)
        if fname == 'write': # write generates our ouput to the html interpreter ==> special handling
            argval = eval_exp(fargs[0], environment)
            output_sofar = env_lookup('javascript output', environment)
            env_update('javascript output', output_sofar + str(argval), environment)
        elif fvalue[0] == "function":
            (fparams, fbody, fenv) = fvalue[1:]
            if len(fparams) != len(fargs):
                print "ERROR: wrong number of args"
            else:
                env_vars = {}
                for param, arg in zip(fparams, fargs):
                    env_vars[param] = eval_exp(arg, environment)
                new_environment = (fenv, env_vars)
                try:
                    eval_stmts(fbody, new_environment)
                    return None
                except Exception as return_value:
                    return return_value
        else:
            print  "ERROR: call to non-function"

#helper proc to simplify eval_exp()
def perform_binop(x, operator, y):
    if operator == '||':
        return x or y
    elif operator == '&&':
        return x and y
    elif operator == '==':
        return x == y
    elif operator == '<':
        return x < y
    elif operator == '>':
        return x > y
    elif operator == '<=':
        return x <= y
    elif operator == '>=':
        return x >= y
    elif operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y

# helper proc to look up variables. begins in the current env frame, bubbles up to global
def env_lookup(vname, environment):
    if vname in environment[1]:
        return (environment[1])[vname]
    elif environment[0] == None:
        return None
    else:
        return env_lookup(vname, environment[0])

# helper proc to update variables. only updates, does not define new variables
def env_update(vname, value, environment):
    if vname in environment[1]:
        (environment[1])[vname] = value
    elif not (environment[0] == None):
        env_update(vname, value, environment[0])

'''
procedure evaluates statements (reminder: statement can include expression, but
not the other way round)

a function call creates a new environment frame as a child of the frame in
which the function is declared. this is to support closures, I'm certain

return statements are implemented using exceptions, I guess as a simple way of
transporting the return payload '''

# helper proc to handle function and if statement bodies (compound stmts)
def eval_stmts(stmts, environment):
    for stmt in stmts:
        eval_stmt(stmt, environment)

def eval_stmt(tree, environment):
    stmttype = tree[0]
    if stmttype == "assign":
        (variable_name, right_child) = tree[1:]
        new_value = eval_exp(right_child, environment)
        env_update(variable_name, new_value, environment)
    elif stmttype == "if-then-else":
        (conditional_exp, then_stmts, else_stmts) = tree[1:]
        if eval_exp(conditional_exp, environment):
            return eval_stmts(then_stmts, environment) # TODO: check stmts is always a list
        else:
            return eval_stmts(else_stmts, environment)
    elif stmttype == "return":
        retval = eval_exp(tree[1], environment)
        raise Exception(retval)
    elif stmttype == "exp":
        eval_exp(tree[1], environment)

def interpret_js(trees):
    global_env = (None, {'javascript output': ''}) # the space in the key prevents conflicts with identifiers
    for tree in trees:
        tree_type = tree[0]
        if tree_type == 'stmt':
            eval_stmt(tree[1], global_env)
        elif tree_type == 'exp':
            eval_exp(tree[1], global_env)
    return global_env[1]['javascript output']

'''
example of a procedure to optimise a js programme (as a parse tree) to remove
unnecessary expressions. we do this before interpreting it, so that we can
arrive at the *same* answer in less time than the original code.

this example is simple, in reality optimisation is a huge deal '''

def optimize(tree):
    elt_type = tree[0]
    if elt_type == "binop":
        (a, op, b) = tree[1:]
        a = optimize(a)
        b = optimize(b)
        if op == "*" and b == ("number","1"):
            return a
        elif op == "*" and b == ("number","0"):
            return ("number","0")
        elif op == "+" and b == ("number","0"):
            return a
        return tree
    return tree

'''
ultimate procedure is to
1. provide words ("word-element","Hello") to a rendering component (missing)
2. invoke js interpreter and render result of script
3. extract and validate tags ('tag-element', 'b', [], [], 'b')] '''

def interpret_html(trees):
    for tree in trees:
        nodetype = tree[0]
        if nodetype == "word_elt":
            word = tree[1]
            print word
        elif nodetype == "tag_elt":
            (tagname, tagargs, subtrees, closetagname) = tree[1:]
            if closetagname != tagname:
                raise Exception('doh! mismatched tags')
            else:
                # placeholder return stmt, pending final spec
                try:
                    interpret_html(subtrees)
                except Exception as problem:
                    print problem
        elif nodetype == 'javascript_elt':
            js_text = tree[1]
            js_ptree = js_parser.parse(js_text, lexer=js_lexer)
            js_ptree = optimize(js_ptree)
            print interpret_js(js_ptree)
