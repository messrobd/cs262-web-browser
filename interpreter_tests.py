from interpreter import *

html_simple = [("word-element","Hello")]
print interpret_html(html_simple)

html_body = [('tag-element', 'body', [], [('tag-element', 'b', [], [('word-element', 'Hello World')], 'b')], 'body')]
print interpret_html(html_body)

html_negative = [('tag-element', 'body', [], [('tag-element', 'i', [], [('word-element', 'Hello World')], 'b')], 'body')]
print interpret_html(html_negative)
