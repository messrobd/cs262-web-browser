precedence = (
    ('left', 'PLUS', 'MINUS'), # lower precedence to the top. left indicates associativity
    ('left', 'TIMES', 'DIVIDE') # higher precedence to the bottom
)

def p_binopt(p):
    '''exp: exp PLUS exp
          | exp MINUS exp
          | exp TIMES exp''' # TODO add remainder
    p[0] = ('binopt', p[1], p[2], p[3])

def p_exp_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ("call", p[1], p[3])

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number", p[1])

def p_optargs(p):
    'optargs : args' # optarg non-terminal must match an input (above)
    p[0] = p[1] # pass on args if there's one or more

def p_optargs_empty(p): # optargs can be empty, not exp. might be why my solution went to infinite recursion
    'optargs : '
    p[0] = []

def p_args(p):
    'args : exp COMMA args' # so I was onto something
    p[0] = [p[1]] + p[3]

def p_args_last(p):
    'args : exp'
    p[0] = [p[1]]
