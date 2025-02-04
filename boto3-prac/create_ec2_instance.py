import boto3
import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

ec2 = boto3.resource("ec2")

instance_params = {"ImageId": "ami-06aa3f7caf3a30282", "KeyName": "hind_aws", "InstanceType": "t2.micro", "MinCount": 1, "MaxCount": 1, "SecurityGroupIds": ["sg-0915b9968ac3df4fa"]}


logging.info("Creating ec2 instance ...")
logging.debug(f"Selecting image id: {instance_params['ImageId']}")
logging.debug(f"Selecting Instance type: {instance_params['InstanceType']}")

instance = ec2.create_instances(**instance_params)

instance[0].wait_until_running()

logging.info("Instance has been started ...")

