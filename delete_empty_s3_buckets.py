import boto3
import pprint

session = boto3.session.Session(profile_name="default", region_name="us-east-1")

def delete_empty_s3_buckets():
    s3_resource = session.resource("s3")
    s3_client = session.client("s3")
    for bucket in s3_resource.buckets.all():
        if "Contents" not in s3_client.list_objects(Bucket=bucket.name):
            print(f"Deleting empty bucket: {bucket.name}")
            bucket.delete()
        else:
            print(f"Skipping non-empty bucket: {bucket.name}")


delete_empty_s3_buckets()