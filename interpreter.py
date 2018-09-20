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
        value = env_lookup(vname,environment)
        if value == None:
            print "ERROR: unbound variable " + vname
        else:
            return value

def perform_binop(x, operator, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y

def env_lookup(vname, environment):
    if vname in environment[1]:
        return (environment[1])[vname]
    elif environment[0] == None:
        return None
    else:
        return env_lookup(vname, environment[0])

def env_update(vname, value, environment):
    if vname in environment[1]:
        (environment[1])[vname] = value
    elif not (environment[0] == None):
        env_update(vname, value, environment[0])

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
    elif stmttype == "call":
        (fname, args) = tree[1:]
        fvalue = env_lookup(fname, environment)
        if fvalue[0] == "function":
            (fparams, fbody, fenv) = fvalue[1:]
            if len(fparams) != len(args):
                print "ERROR: wrong number of args"
            else:
                env_vars = {}
                for param, arg in zip(fparams, args):
                    env_vars[param] = eval_exp(arg, environment)
                new_environment = (fenv, env_vars) # parent env should be that of the func declaration
                try:
                    eval_stmts(fbody, new_environment)
                    return None
                except Exception as return_value:
                    return return_value
        else:
            print  "ERROR: call to non-function"
    elif stmttype == "return":
        retval = eval_exp(tree[1],environment)
        raise Exception(retval)
    elif stmttype == "exp":
        eval_exp(tree[1],environment)

def eval_stmts(stmts, environment):
    for stmt in stmts:
        eval_stmt(stmt, environment)
