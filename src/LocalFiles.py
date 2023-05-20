import tempfile
import datetime
import json
import logging
import os

class LocalFiles:

    @staticmethod
    def save_var_temp_file(data):
        if type(data) == dict:
            #json
            filename = str(int(datetime.datetime.now().timestamp()))
            temp = tempfile.NamedTemporaryFile(prefix = filename, suffix='.json', delete=False)
            temp.close()
            print(temp.name)
            with open(temp.name, 'w') as f:
                f.write(json.dumps(data))

            with open(temp.name, 'r') as f:
                print(f.read())

            return temp.name
        if type(data) == list:
            #csv
            return

    @staticmethod
    def delete_temp_file(temp_path):
        try:
            os.remove(temp_path)
            logging.info('{} deleted'.format(temp_path))
            return 
        except Exception as e:
            logging.error(str(e))

if __name__ == '__main__':
    data = {'test key': 'test val'}
    temp_name = LocalFiles.save_var_temp_file(data)
    LocalFiles.delete_temp_file(temp_name)