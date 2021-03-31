# Example way to run the script with a Lambda Function name and ARN:
# python .\lambda.py hellpythonlambda arn:aws:iam::912101370089:role/service-role/cloudskillslambdarole

import boto3
import botocore
import sys
import logging


def create_lambda(name, role):
    try:
        client = boto3.client('lambda')

        filePath = "./pythonscript.zip"

        client.create_function(
            FunctionName=name,
            Runtime='python3.8',
            Role=role,
            Handler='lambda_handler',
            Code={'ZipFile': open(filePath, 'rb').read(), },
        )
    
    except botocore.exceptions.ClientError as error:
        raise error
    
    except botocore.exceptions.ParamValidationError as e:
        logging.exception(e)


name = sys.argv[1]
role = sys.argv[2]

if __name__ == '__main__':
    create_lambda(name, role)