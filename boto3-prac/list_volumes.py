import boto3



ec2 = boto3.resource("ec2")



print(f"Checking vols")
for vol in ec2.volumes.all():
    vol.create_snapshot(VolumeId=vol.id, Description="Kashi boto3 managed snapshot")
