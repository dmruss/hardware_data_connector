from SystemData import SystemData
from LocalFiles import LocalFiles
from AWSUtils import AWSUtils
import time

def main():
    data = SystemData.get_sys_data()
    temp_file_path, filename = LocalFiles.save_var_temp_file(data)
    aws_connection = AWSUtils()
    aws_connection.s3_upload_file(temp_file_path, filename)
    LocalFiles.delete_temp_file(temp_file_path)


def main_local_test():
    while True:
        print(SystemData.get_sys_data())
        time.sleep(10)

if __name__ == '__main__':
    main()