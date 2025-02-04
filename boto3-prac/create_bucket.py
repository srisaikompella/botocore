import logging
import boto3

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

printer = logging.StreamHandler()

formati_ = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

printer.setFormatter(formati_)

logger.addHandler(printer)

logger.info("I am kashi ...")

from botocore.exceptions  import ClientError


def create_buck(name, region=None):

    try:
        if region is None:
            s3 = boto3i.client("s3")
            s3.create_bucket(Bucket=name)
        else:
            s3 = boto3.client("s3", region_name=region)
            location  = {'LocationConstraint': region}
            s3.create_bucket(Bucket=name,  CreateBucketConfiguration=location)
    except ClientError as e:
        logger.error(e)
        return False
    return True


name = input("enter bucket name: ")
region = input("enter region name: ")
if create_buck(name, region):
    logger.info("Bucket has been created ...")
else: 
    logger.error("Error !!!!")
