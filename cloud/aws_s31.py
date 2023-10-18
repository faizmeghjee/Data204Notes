import boto3
from pprint import pprint

s3_client = boto3.client('s3') # lower level service
s3_resource = boto3.resource('s3')

bucket_list = s3_client.list_buckets()

pprint(bucket_list)