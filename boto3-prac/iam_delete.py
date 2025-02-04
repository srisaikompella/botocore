import boto3


iam = boto3.resource("iam")


for idx, user in enumerate(iam.users.all()):
    if user.name != "test":
        print(f"deleting {user.name}")
        user.delete()
    else:
        print("Skipping test ...")
