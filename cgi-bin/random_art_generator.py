#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import random

form = cgi.FieldStorage()
canvas_size = form.getvalue("canvas-size")

def generate_random_art(canvas_size):
    try:
        canvas_size = int(canvas_size)
        random_art = ""
        for _ in range(canvas_size):
            row = ""
            for _ in range(canvas_size):
                color = f"{random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}"
                pixel = f"<span style='background-color: rgb({color});'>&nbsp;&nbsp;</span>"
                row += pixel
            random_art += f"<div>{row}</div>"
        return random_art
    except ValueError:
        return "Please enter a valid canvas size."

result = generate_random_art(canvas_size)
print(f"<div class='result'>{result}</div>")

