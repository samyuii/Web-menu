[200~#!/usr/bin/env python3
  import cgi
  import os

  form = cgi.FieldStorage()

  print("Content-type: text/html\n")

  if "file" in form:
      uploaded_photo = form["file"]
      if uploaded_photo.filename:
          filename = os.path.basename(uploaded_photo.filename)
          with open(os.path.join('uploads', filename), 'wb') as f:
              f.write(uploaded_photo.file.read())
          print("Image uploaded successfully!")
  else:
      print("No file uploaded.")
