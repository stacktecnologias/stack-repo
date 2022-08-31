#lendo e escrevendo arquivos co o boto3

import sys
import io
import os 
import pandas as pd
import boto3
from botocore.exceptions import ClientError
from datetime import datetime



client = boto3.client(service_name='s3', 
region_name='us-east-1', 
aws_access_key_id='CHAVE_DO_USUARIO', 
aws_secret_access_key='CHAVE_DO_USUARIO'
)

s3_client = boto3.client('s3')
S3_BUCKET = 's3boto3'
S3_PREFIX = 'ler/'   
response = s3_client.list_objects_v2(
    Bucket=S3_BUCKET, Prefix=S3_PREFIX, StartAfter=S3_PREFIX,)
s3_files = response["Contents"]
for s3_file in s3_files:
    print("s3_file")
    df1 = pd.read_csv(s3_client.get_object(
        Bucket=S3_BUCKET, Key=s3_file["Key"]).get("Body"))
    


print(df1)


df1=df1.drop(['AREA'], axis=1)

print("arquivo alterado")
print(df1)


df1.to_csv('arquivoalterado')


with open('arquivoalterado', 'rb') as f:
    s3_client.upload_fileobj(f, "s3boto3", "arquivoalterado" + datetime.now().strftime("%Y%m%d-%I:%M:%S%p"))

