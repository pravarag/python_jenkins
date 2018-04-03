#!/usr/bin/python

import boto3

from boto3.session import Session

session=Session(aws_access_key_id='', aws_secret_access_key='')

session=boto3.Session(profile_name='test')

s3=boto3.client('s3')

s3.create_bucket(Bucket='pravarbucket2')
