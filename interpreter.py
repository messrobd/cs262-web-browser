'''
procedure is to provide words ("word-element","Hello") to a rendering component
(missing) and to extract and validate tags ('tag-element', 'b', [], [], 'b')]'''

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
