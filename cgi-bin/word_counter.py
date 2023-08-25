#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi

form = cgi.FieldStorage()
text_to_count = form.getvalue("text-to-count")

def count_words(text):
    if text is None:
        return ""
    words = text.split()
    word_count = len(words)
    return f"Word count: {word_count}"

result = count_words(text_to_count)
print(f"<div class='result'>{result}</div>")

