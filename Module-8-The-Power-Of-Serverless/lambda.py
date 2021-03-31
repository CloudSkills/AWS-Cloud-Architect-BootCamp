import boto3
import botocore
import sys
import logging

def create_lambda(name):
    try:
        client = boto3.client('lambda')

        client.create_function(
            FunctionName=name,
            Runtime='python3.8',
            Role="",
        )
    
    except botocore.exceptions.ClientError as error:
        raise error

    except botocore.exceptions.ResourceConflictExcept as conflict:
        print(conflict)

    except botocore.exceptions.ParamValidationError as e:
        logging.exception('Parameter Validation: %s' & e)

name = sys.argv[1]

if __name__ == '__main__':
    create_lambda(name)