# Run the following
# python start_ec2instance.py 

import boto3


ec2 = boto3.client('ec2')

def start_ec2instance():
    
    ec2.start_instances(InstanceIds= ['i-0ee408a52dd96dbb0'])

start_ec2instance()