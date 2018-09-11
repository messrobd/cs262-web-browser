def p_binopt(p):
    '''exp: exp PLUS exp
          | exp MINUS exp
          | exp TIMES exp''' # TODO add remainder
    p[0] = ('binopt', p[1], p[2], p[3])

precedence = (
    ('left', 'PLUS', 'MINUS'), # lower precedence to the top. left indicates associativity 
    ('left', 'TIMES', 'DIVIDE') # higher precedence to the bottom
)
