#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import os
import boto3

# Set your AWS access key and secret key as environment variables
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA5Z6E62QUMRWCBRXR'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'tYa29dYwYRhmmAxUgI+RgvHJS6etxwZGMVRtEdXc'

form = cgi.FieldStorage()
bucket_name = form.getvalue("bucket-name")

if bucket_name:
    try:
        s3_client = boto3.client('s3', region_name='ap-south-1')
        s3_client.create_bucket(
            Bucket=bucket_name,
            ACL='private',
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            }
        )
        print("<h2>Bucket created successfully.</h2>")
    except Exception as e:
        print("<h2>Error creating bucket:", e, "</h2>")
else:
    print("<h2>Please enter a bucket name.</h2>")

