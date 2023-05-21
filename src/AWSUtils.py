import boto3
import logging
import json


class AWSUtils:

    def __init__(self):
        self.s3 = boto3.client('s3')
        with open('./src/config.json', 'r') as f:
            contents = json.load(f)
            self.bucket_name = contents['bucket_name']
            self.tenant_name = contents['tenant_name']
            self.app_name = contents['app_folder']
            self.stream_name = contents['kinesis_stream']

    def s3_upload_file(self, local_path, filename):
        try:
            self.s3.upload_file(
                Filename=local_path,
                Bucket=self.bucket_name,
                Key='{}/{}'.format(self.app_name, filename)
            )
        except Exception as e:
            logging.error(str(e))

    def kinesis_put_record(self, data):
        try:
            kinesis = boto3.client('kinesis')
            response = kinesis.put_record(
                StreamName=self.stream_name,
                Data=json.dumps(data),
                PartitionKey='test_key'
            )
            print('successfully added to stream')
            print(response)
        except Exception as e:
            print(e)