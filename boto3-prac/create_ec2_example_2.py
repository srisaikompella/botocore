import boto3


ec2 = boto3.resource("ec2")

#ec2 = boto3.client("ec2")

#sec = ec2.create_security_group(Description='boto3 managed security group', DryRun=False, GroupName='boto3-sg-test')


#authorize_sec = ec2.authorize_security_group_ingress(GroupName=sec.group_name, FromPort=22, CidrIp="0.0.0.0/0", IpProtocol="TCP", ToPort="22")

#print(authorize_sec)

print("creating instance ...")

instance = ec2.create_instances(ImageId='ami-06aa3f7caf3a30282', InstanceType='t2.micro', KeyName='test_aws', SecurityGroupIds=['sg-0915b9968ac3df4fa'], MaxCount=1, MinCount=1)

instance = instance[0]

instance.wait_until_running()

print("instance created .." )
