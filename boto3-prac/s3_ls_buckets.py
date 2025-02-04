import boto3


s3 = boto3.client("s3")

for i in  s3.list_buckets()["Buckets"]:
    print(i["Name"])
