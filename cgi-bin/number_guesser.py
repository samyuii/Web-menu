#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import random

form = cgi.FieldStorage()
guessed_number = form.getvalue("guessed-number")

# Generate a random target number between 1 and 100
target_number = random.randint(1, 100)

def compare_numbers(target, guessed):
    if guessed is None:
        return ""
    if target < guessed:
        return "Too high! Try again."
    elif target > guessed:
        return "Too low! Try again."
    else:
        return f"Congratulations! You guessed the number {target} correctly!"

try:
    guessed_number = int(guessed_number) if guessed_number else None
    result = compare_numbers(target_number, guessed_number)
except (ValueError, TypeError):
    result = "Please enter valid numbers."

print(f"<div class='result'>{result}</div>")

