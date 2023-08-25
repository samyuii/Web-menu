#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi

form = cgi.FieldStorage()
latitude = form.getvalue("latitude")
longitude = form.getvalue("longitude")

def check_coordinate(lat, long):
    if lat is None or long is None:
        return ""
    if -90 <= float(lat) <= 90 and -180 <= float(long) <= 180:
        return "Valid coordinates."
    else:
        return "Invalid coordinates."

result = check_coordinate(latitude, longitude)
print(f"<div class='result'>{result}</div>")

