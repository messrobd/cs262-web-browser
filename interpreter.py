'''
procedure is to provide words ("word-element","Hello") to a rendering component
(missing) and to extract and validate tags ('tag-element', 'b', [], [], 'b')]

missing: don't yet see how we are going tp transition from html to js
interpreter '''

def interpret_html(trees):
    for tree in trees:
        nodetype = tree[0]
        if nodetype == "word-element":
            word = tree[1]
            return word
        elif nodetype == "tag-element":
            (tagname, tagargs, subtrees, closetagname) = tree[1:]
            if closetagname != tagname:
                raise Exception('doh! mismatched tags')
            else:
                # placeholder return stmt, pending final spec
                try:
                    return tagname + ' ' + interpret_html(subtrees)
                except Exception as problem:
                    print problem

def eval_exp(tree, environment):
    nodetype = tree[0]
    if nodetype == "number":
        return float(tree[1])
    elif nodetype == "string":
        return tree[1]
    elif nodetype == "true":
        return True
    elif nodetype == "false":
        return False
    elif nodetype == "not":
        return not(eval_exp(tree[1], environment))
    elif nodetype == "binop":
        (left_child, operator, right_child) = tree[1:]
        x = eval_exp(left_child, environment)
        y = eval_exp(right_child, environment)
        return perform_binop(x, operator, y)
    elif nodetype == "identifier":
        return env_lookup(environment, tree[1])

def perform_binop(x, operator, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    
def env_lookup(env,vname):
        return env.get(vname,None)
