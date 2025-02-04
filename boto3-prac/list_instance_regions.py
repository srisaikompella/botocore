import boto3


ec2 = boto3.resource("ec2")

regions = ec2.meta.client.describe_regions()['Regions']

a = []

for i in regions:
    a.append(i['RegionName'])


for i in a:
    print(f"Checking region {i}")
    obj = boto3.resource("ec2", region_name=i)
    for i in obj.instances.filter(Filters=[{'Name': 'instance-state-name', "Values": ["running"]}]):
        print(i.id)

