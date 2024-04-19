sessions:
nothing but used to authenticate with the aws account.
1) default sessions used for default profiles -> boto3.session.Session()
2) custom session used for custom profiles -> boto3.session.Session(profile_name="hind")


client:
1) provides low level aws svc access.
2) original boto3 api abstraction
3) all aws svc ops are supported

resource:
1) provides high level, obj oriented API
2) newer boto3 api abstraction
3) does not provide 100% api coverage of aws svcs.



Check if you are able to access the aws:

import boto3
sts = boto3.client("sts")
sts.get_caller_identity()

example - response::
```
>>> sts.get_caller_identity()
{'UserId': 'AROA33UURRMLUTLD3LWUV:botocore-session-1708967423', 'Account': '815281572631', 'Arn': 'arn:aws:sts::815281572631:assumed-role/wl_juniper/botocore-session-1708967423', 'ResponseMetadata': {'RequestId': '5db1ae62-a4d2-4420-b6de-734129735a39', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '5db1ae62-a4d2-4420-b6de-734129735a39', 'content-type': 'text/xml', 'content-length': '471', 'date': 'Mon, 26 Feb 2024 17:10:35 GMT'}, 'RetryAttempts': 0}}
```

Check diff between resource && client:

sess = boto3.session.Session()
sess.get_avaialble_services()
example - response::
```
['accessanalyzer', 'account', 'acm', 'acm-pca', 'alexaforbusiness', 'amp', 'amplify', 'amplifybackend', 'amplifyuibuilder', 'apigateway', 'apigatewaymanagementapi', 'apigatewayv2', 'appconfig', 'appconfigdata', 'appfabric', 'appflow', 'appintegrations', 'application-autoscaling', 'application-insights', 'applicationcostprofiler', 'appmesh', 'apprunner', 'appstream', 'appsync', 'arc-zonal-shift', 'athena', 'auditmanager', 'autoscaling', 'autoscaling-plans', 'b2bi', 'backup', 'backup-gateway', 'backupstorage', 'batch', 'bcm-data-exports', 'bedrock', 'bedrock-agent', 'bedrock-agent-runtime', 'bedrock-runtime', 'billingconductor', 'braket', 'budgets', 'ce', 'chime', 'chime-sdk-identity', 'chime-sdk-media-pipelines', 'chime-sdk-meetings', 'chime-sdk-messaging', 'chime-sdk-voice']#### Output omitted.
sess.get_available_resources()
example - response::
['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
```

understand why client is lower level api and resource is high level & obj oriented:

Client implementation
```
>>> sess = boto3.session.Session()
>>> c_cli = sess.client("iam")
>>> for i in c_cli.list_users()['Users']:
...   print(i['UserName'])
... 
test
>>> 
Resource implementation
>>> for i in c_res.users.all():
...    print(i.name)
... 
test
>>> 
```


Paginator: If you are trying to retrieve more than one page of result, we need to use this. with client, one page for IAM is 100 and for s3 it is 1000.

Meta: If some operation is not supported by a region and if it is only supported by a client we can use meta to utilise the client features to perform the operation.

[ex]: client can describe all the regions using describe_regions() method. whereas the resource do not contain any method to list the available regions in an aws account.


