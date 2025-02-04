import boto3

ec2 = boto3.resource("ec2")

filtered = ec2.instances.filter(Filters=[{'Name': 'instance-type', 'Values':['t2.micro']}])

print(filtered)

for i in filtered:
    print(i.state['Name'])
