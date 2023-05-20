from SystemData import SystemData
from LocalFiles import LocalFiles
from AWSUtils import AWSUtils
import time
import sys

def main(mode):
    aws_connection = AWSUtils()
    data = SystemData.get_sys_data()
    data = SystemData.add_tenant_name(data, aws_connection.tenant_name)
    if mode == 'kinesis':
        aws_connection.kinesis_put_record(data)
    elif mode == 's3':
        temp_file_path, filename = LocalFiles.save_var_temp_file(data)
        aws_connection.s3_upload_file(temp_file_path, filename)
        LocalFiles.delete_temp_file(temp_file_path)
    else:
        print('Unknown mode selected')


def main_local_test():
    while True:
        print(SystemData.get_sys_data())
        time.sleep(10)

if __name__ == '__main__':
    mode = sys.argv[1]
    while True:
        main(mode)