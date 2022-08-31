#Criando cluster com o btoto 3

import sys
import io
import os 
import json
import boto3
from botocore.exceptions import ClientError

client = boto3.client(
    'emr', 
    region_name='us-east-1',
    aws_access_key_id='CHAVE_DO_USUARIO',
    aws_secret_access_key='CHAVE_DO_USUARIO'
    )

response = client.run_job_flow (
    Name="EMR-Boto3-Aula",
    ReleaseLabel='emr-6.3.0',
    LogUri='s3://aws-logs-300162418540-us-east-1/elasticmapreduce/',
    Applications=[{'Name': 'Hadoop'}, {'Name': 'Spark'}],
    Instances = 
    {
        'InstanceGroups': [
            {
                'Name': "Master nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'r5.2xlarge',
                'InstanceCount': 1,
            },
            {
                'Name': "Slave nodes",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'r5.2xlarge',
                'InstanceCount': 2,
            },
        ],
        'TerminationProtected': False,
        'Ec2KeyName': 'AulaEMRSpark',
    },
      
    VisibleToAllUsers=True,
    ServiceRole='EMR_DefaultRole',
    JobFlowRole='EMR_EC2_DefaultRole',
    AutoScalingRole="EMR_AutoScaling_DefaultRole"
)

print (json.dumps(response, indent=4, sort_keys=True, default=str))
