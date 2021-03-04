# Run the following
# python stop_ec2instance.py 

import boto3


ec2 = boto3.client('ec2')

def stop_ec2instance():
    
    ec2.stop_instances(InstanceIds= ['i-06be78226da26a405'])

stop_ec2instance()