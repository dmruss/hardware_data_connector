from SystemData import SystemData
import time

def main():
    while True:
        print(SystemData.get_sys_data())
        time.sleep(10)


if __name__ == '__main__':
    main()