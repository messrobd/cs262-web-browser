def p_binopt(p):
    '''exp: exp PLUS exp
          | exp MINUS exp 
          | exp TIMES exp''' # TODO add remainder
    p[0] = ('binopt', p[1], p[2], p[3])
