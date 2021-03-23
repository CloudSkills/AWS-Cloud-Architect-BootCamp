# Run the following
# python stop_ec2instance.py 

import boto3
import sys


ec2 = boto3.client('ec2')

def stop_ec2instance(instanceID):
    
    ec2.stop_instances(InstanceIds= [instanceID])

instanceID = sys.argv[1]

stop_ec2instance(instanceID)