import graphics

def interpret(trees): # Hello, friend
    for tree in trees: # Hello,
        # ("word-element","Hello")
        nodetype=tree[0] # "word-element"
        if nodetype == "word-element":
            #graphics.word(tree[1])
            return tree[1]
        elif nodetype == "tag-element":
            # <b>Strong text</b>
            tagname = tree[1] # b
            tagargs = tree[2] # []
            subtrees = tree[3] # ...Strong Text!...
            closetagname = tree[4] # b
            # QUIZ: (1) check that the tags match
            # if not use graphics.warning()
            #  (2): Interpret the subtree
            # HINT: Call interpret recursively
            if closetagname != tagname:
                graphics.warning('doh! mismatched tags')
            else:
                return tagname + ' ' + interpret(subtrees)

#graphics.initialize() # Enables display of output.\
#interpret([("word-element","Hello")])
#graphics.finalize() # Enables display of output.

html_simple = [("word-element","Hello")]
print interpret(html_simple)

html_body = [('tag-element', 'body', [], [('tag-element', 'b', [], [('word-element', 'Hello World')], 'b')], 'body')]
print interpret(html_body)
