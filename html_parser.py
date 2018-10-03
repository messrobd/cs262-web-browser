'''
rules:
html => elt html # the first recognised element, followed by the rest of the content
html =>          # the rest of the content may be empty
elt => WORD      # an element can be a word, which is a terminal
elt => tag
tag => < WORD opt_args > html < / WORD >
opt_args => tag_args
opt_args =>
tag_args => WORD tag_args
tag_args => WORD                                                             '''

from html_lexer import tokens

def p_html(p): # p_ is the flag prefix for a parse rule
    'html : elt html' # my guess this is interpreted as an object
    p[0] = [p[1]] + p[2] # p[0] refers to 'html' on the lhs (is looking up from the 'object'?)
                     # p[1] refers to elt, and p[2] to the remaining html, return 1 list

def p_html_empty(p):
    'html : '
    p[0] = [ ]

def p_elt_word(p):
    'elt : WORD' # capitalisation signifies a TOKEN (previously defined)
    p[0] = ('word_elt', p[1]) # I think this will always substitute, rather than nesting

'''
example:
html = "Rama's journey"
parse_tree = [
    ('word_elt', 'Rama's),
    ('word_elt', 'journey')] '''

def p_elt_javascript(p):
    'elt : JAVASCRIPT'
    p[0] = ('javascript_elt', p[1])

def p_elt_tag(p):
    'elt : LANGLE WORD opt_args RANGLE html LANGLESLASH WORD RANGLE'
    p[0] = ('tag_elt', p[2], p[3], p[5], p[7]) # WORD's are terminals, tag_args & html get expanded

def p_opt_args(p):
    'opt_args : tag_args'
    p[0] = p[1]

def p_opt_args_empty(p):
    'opt_args : '
    p[0] = [ ]

def p_tag_args(p):
    'tag_args : WORD tag_args'
    p[0] = [p[1]] + p[2]

def p_tag_args_last(p):
    'tag_args : WORD'
    p[0] = [p[1]]

'''
example:
html = "hello <b>baba</b> yaga"
parse_tree = [
    ('word_elt', 'hello'),
    ('tag_elt', 'b', [], [('word_elt', 'baba')]), # html got expanded into its own parse tree
    ('word_elt', 'yaga')] '''
