import boto3


iam = boto3.client("iam")

paginator = iam.get_paginator('list_users')

iterator = paginator.paginate()

c=0

for i in iterator:
    a = i['Users']
    for j in a:
        print(c, j['UserName'])
        c+=1
