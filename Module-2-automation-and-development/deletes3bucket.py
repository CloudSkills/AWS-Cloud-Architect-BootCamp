import boto3
import sys


def main():
    deletes3bucket(name)

def deletes3bucket(name):
    client = boto3.client('s3')

    delete = client.delete_bucket(
        Bucket=name,
    )

    print(delete)


name = sys.argv[1]


if __name__ == '__main__':
    main()