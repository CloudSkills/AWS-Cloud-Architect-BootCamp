# Ensure to have the libraries needed:
# 1. pip install mysql-replication
# 2. pip install boto3
# 3. pip install pymysql


import json
import sys

import boto3
import pymysql_utils
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent


def main():
    kinesis_stream(host, sqluser, password, streamname)


def kinesis_stream(host, sqluser, password, streamname):
  client = boto3.client("kinesis")

  # MySQL Connection Info
  connection = {
      "host": host,
      "port": 3306,
      "user": sqluser,
      "passwd": password
  }

  stream = BinLogStreamReader(
    connection_settings = connection,
    server_id=100,
    blocking=True,
    resume_stream=True,
    only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent])


  for binlogevent in stream:
    for row in binlogevent.rows:
      event = {"schema": binlogevent.schema,
      "table": binlogevent.table,
      "type": type(binlogevent).__name__,
      "row": row
      }

      client.put_record(StreamName=streamname, Data=json.dumps(event), PartitionKey="default")
      print(json.dumps(event))



host = sys.argv[1]
sqluser = sys.argv[2]
password = sys.argv[3]
streamname = sys.argv[4]


if __name__ == "__main__":
   main()