#Criando e destruindo buckets com o boto3
import sys
import io
import os 
import boto3
from botocore.exceptions import ClientError

client = boto3.client(service_name='s3', 
region_name='us-east-1', 
aws_access_key_id='CHAVE_DO_USUARIO', 
aws_secret_access_key='CHAVE_DO_USUARIO'
)

s3_client = boto3.client('s3')
s3 = boto3.client('s3')



response = s3.list_buckets()
print('Buckets Existentes:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

print("CRIA UM BUCKET")
s3_client.create_bucket(Bucket="criando-teste")



response = s3.list_buckets()
print('Buckets Existentes:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

print("DELETA UM BUCKET")
s3_client.delete_bucket(Bucket="deletando-teste")



response = s3.list_buckets()
print('Buckets Existentes:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
