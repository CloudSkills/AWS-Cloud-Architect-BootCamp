import boto3
import sys


def main():
    creates3bucket(name)

def creates3bucket(name):
    client = boto3.client('s3')

    create = client.create_bucket(
        ACL='private',
        Bucket=name,
    )

    print(create)


name = sys.argv[1]


if __name__ == '__main__':
    main()