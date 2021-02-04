import boto3
import sys


def main():
    deletes3bucket(name)

def deletes3bucket(name):
    client = boto3.client('s3')

    create = client.delete_bucket(
        Bucket=name,

    )

    print(create)


name = sys.argv[1]


if __name__ == '__main__':
    main()