#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import smtplib, ssl

form = cgi.FieldStorage()
receiver_email = form.getvalue("to")
subject = form.getvalue("subject")
message_email = form.getvalue("message")

if receiver_email and subject and message_email:
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "jainsamyak170@gmail.com"
    password = "gkon xpwm dcjz gsiu"

    email_message = f"Subject: {subject}\n\n{message_email}"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_message)

    print("<h2>Email sent successfully.</h2>")
else:
    print("<h2>Please enter receiver email, subject, and message.</h2>")
