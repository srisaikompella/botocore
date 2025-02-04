import boto3 as b


iam = b.resource("iam")


for i in range(1,151):
    iam_params = {"UserName": f"kashi-{i}"}
    print(f"Creating user - {iam_params['UserName']}")
    iam.create_user(**iam_params)
    print(f"Created ...")

