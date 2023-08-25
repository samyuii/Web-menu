#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import pywhatkit as kit

form = cgi.FieldStorage()
phone_number = form.getvalue("phone-number")
message = form.getvalue("message")

def send_whatsapp(phone, msg):
    try:
        kit.sendwhatmsg(phone, msg, 0, 0)  # Sending immediately
        return "WhatsApp message sent successfully."
    except Exception as e:
        return f"Error sending WhatsApp message: {e}"

if phone_number and message:
    result = send_whatsapp(phone_number, message)
else:
    result = "Please enter phone number and message."

print(f"<div class='result'>{result}</div>")

