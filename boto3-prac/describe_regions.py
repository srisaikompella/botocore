import boto3


ec2 = boto3.resource("ec2")


ec2.meta.client.stop_instances(InstanceIds=["i-02c0326b67ea049be"])

print("stopping instance. ..")

waiter  = ec2.meta.client.get_waiter('instance_stopped')
waiter.wait(InstanceIds=["i-02c0326b67ea049be"])


print("Instance has been stopped...")
