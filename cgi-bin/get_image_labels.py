#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import boto3

def detect_labels(image_bytes):
    aws_access_key = 'AKIAQJYDURIUH7ASYGEB'
    aws_secret_key = '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'
    
    client = boto3.client('rekognition', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='ap-south-1')

    response = client.detect_labels(Image={'Bytes': image_bytes})

    return response['Labels']

form = cgi.FieldStorage()
image_file = form['image']

if image_file.filename:
    image_bytes = image_file.file.read()
    labels = detect_labels(image_bytes)

    print("<h2>Labels in the image:</h2>")
    for label in labels:
        label_name = label['Name']
        confidence = label['Confidence']
        print(f"<p>- {label_name} (Confidence: {confidence:.2f}%)</p>")
else:
    print("<h2>No image uploaded.</h2>")

