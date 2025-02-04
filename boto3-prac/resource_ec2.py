import boto3

ec2 = boto3.resource("ec2")

instance = ec2.Instance("i-02859eabcde2e11a7")


print(f"State of the instance is : {instance.state}")

def stop_instance(instance_id):
    print("stop an ec2 instance")
    instance.stop()
    instance.wait_until_stopped()
    print("stopped")
def start_instance(instance_id):
    print("starting an instance")
    instance.start()
    instance.wait_until_running()
    print("started")

def ec2_terminate(instance_id):
    print("terminating an ec2 instance")
    instance.terminate()
    instance.wait_until_terminated()
    print("terminated")

#if instance.state['Name'] == "running":
#    stop_instance("i-02859eabcde2e11a7")
#else:
#    start_instance("i-02859eabcde2e11a7")
