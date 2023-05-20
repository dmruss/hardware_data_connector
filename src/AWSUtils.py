import boto3
import logging
import json
import datetime


class AWSUtils:

    def __init__(self):
        self.s3 = boto3.client('s3')
        with open('config.json', 'r') as f:
            contents = json.load(f)
            self.bucket_name = contents['bucket_name']
            self.tenant_name = contents['tenant_name']

    def s3_upload_file(self, local_path, filename):
        try:
            self.s3.upload_file(
                Filename=local_path,
                Bucket=self.bucket_name,
                Key='{}/{}'.format(self.tenant_name, filename)
            )
        except Exception as e:
            logging.error(str(e))
