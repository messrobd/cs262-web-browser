'''
parsing JS statements (lesson 16: prob set 4, #4)

complete the JS parser for statements. grammar:
    js => element js                                            # starting non-terminal. recursive term
    js =>                                                       # js base case
    element => FUNCTION IDENTIFIER ( optparams ) compoundstmt   # function declaration element
    element => stmt ;                                           # statement element
    optparams =>                                                # no params
    optparams => params                                         # >= 1 params
    params => IDENTIFIER , params                               # >1 params. recursive term
    params => IDENTIFIER                                        # base case, ==1 params
    compoundstmt => { statements }                              # body of the func
    statements => stmt ; statements                             # recursive term
    statement =>                                                # base case
    stmt => IF exp compoundstmt
    stmt => IF exp compoundstmt ELSE compoundstmt
    stmt => IDENTIFIER = exp
    stmt => RETURN exp
    stmt => VAR IDENTIFIER = exp
    stmt => exp
    [exp => IDENTIFIER]                                         # exercise treats all exp as identifiers
'''

start = 'js'    # label the starting non-terminal

def p_js(p):
        'js : element js'
        p[0] = [p[1]] + p[2]

def p_js_empty(p):
        'js : '
        p[0] = [ ]

# desired parse tree: ('function', name, args, body)
def p_element_func(p):
    'element : FUNCTION IDENTIFIER LPAREN optparams RPAREN compoundstmt'
    p[0] = ('function', p[2], p[4], p[6])

# desired parse tree: ('stmt', stmt)
def p_element_stmt(p):
    'element : stmt SEMICOLON'
    p[0] = ('stmt', p[1])

def p_optparams(p):
    'optparams : params'
    p[0] = p[1]

def p_optparams_empty(p):
    'optparams : '
    p[0] = [ ]

def p_params(p):
    'params : IDENTIFIER COMMA params'
    p[0] = [p[1]] + p[3]

def p_params_last(p):
    'params : IDENTIFIER'
    p[0] = [p[1]]

def p_compoundstmt(p):
    'compoundstmt : LBRACE statements RBRACE'
    p[0] = p[2]

def p_statements(p):
    'statements : stmt SEMICOLON statements'
    p[0] = [p[1]] + p[3]

def p_statements_empty(p):
    'statements : '
    p[0] = [ ]

# desired pt: ('if-then', conditional, then_branch)
def p_stmt_ifthen(p):
    'stmt : IF exp compoundstmt'
    p[0] = ('if-then', p[2], p[3])

# desired pt: ('if-then-else', conditional, then_branch, else_branch)
def p_stmt_ifthenelse(p):
    'stmt : IF exp compoundstmt ELSE compoundstmt'
    p[0] = ('if-then-else', p[2], p[3], p[5])

# desired pt: ('assign', identifier, new_value)
def p_stmt_assign(p):
    'stmt : IDENTIFIER EQUAL exp'
    p[0] = ('assign', p[1], p[3])

# desired pt: ('return' exp)
def p_stmt_return(p):
    'stmt : RETURN exp'
    p[0] = ('return', p[2])

# desired pt: ('var', identifier, initial_value)
def p_stmt_declare(p):
    'stmt : VAR IDENTIFIER EQUAL exp'
    p[0] = ('var', p[2], p[4])

# desired pt: ('exp', exp)
def p_stmt_exp(p):
    'stmt : exp'
    p[0] = ('exp', p[1])

def p_exp_identifier(p): # placeholder for exercise 4
        'exp : IDENTIFIER'
        p[0] = ("identifier",p[1])

''' to be developed in exercise 5
precedence = (
    ('left', 'PLUS', 'MINUS'), # lower precedence to the top. left indicates associativity
    ('left', 'TIMES', 'DIVIDE') # higher precedence to the bottom
)

def p_binopt(p):
    \'''exp: exp PLUS exp
          | exp MINUS exp
          | exp TIMES exp\''' # TODO add remainder
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
'''
