#!/usr/bin/python3
print("Content-type:text/html")
print()

import cgi
import boto3
import os

# Set your AWS access key and secret key as environment variables
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA5Z6E62QUMRWCBRXR'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'tYa29dYwYRhmmAxUgI+RgvHJS6etxwZGMVRtEdXc'

form = cgi.FieldStorage()
instance_name = form.getvalue("instance-name")

if instance_name:
    try:
        region = 'ap-south-1'  # Update with your desired region
        ec2_client = boto3.client('ec2', region_name=region)
        response = ec2_client.run_instances(
            ImageId='ami-0da59f1af71ea4ad2',  # Update with your desired AMI ID
            InstanceType='t2.micro',
            MaxCount=1,
            MinCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': instance_name
                        },
                    ]
                },
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"<h2>Instance launched successfully. Instance ID: {instance_id}</h2>")
    except Exception as e:
        print("<h2>Error launching instance:", e, "</h2>")
else:
    print("<h2>Please enter instance name.</h2>")

