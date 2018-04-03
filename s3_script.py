#!/usr/bin/python

import boto3

from boto3.session import Session

session=Session(aws_access_key_id='AKIAJTN7IEMUD5BAC7UQ', aws_secret_access_key='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')

session=boto3.Session(profile_name='test')

s3=boto3.client('s3')

s3.create_bucket(Bucket='pravarbucket2')