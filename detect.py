import os
import time
import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--time_gap', type=int, default=30, help='how many time to detect the model, and the unit is minute')
parser.add_argument('--path', type=str, default='/home/mod/PycharmProjects/run_app/api.py',
                    help='python path of you want to detect')
args = parser.parse_args()


if __name__ == '__main__':
    gap_minute = args.time_gap
    while True:
        print('--------------------开始检测-----------------------')
        try:
            # 访问的应用接口
            is_free = requests.get('http://127.0.0.1:8000/is_free')
            if is_free.text == '1':
                # 若访问某个接口的状态码不正确，运行另一个脚本以杀死某一程序
                response = requests.post('http://127.0.0.1:8000/', json={"message": "你好"},
                                         headers={'Content-Type': 'application/json'})
                if response.status_code != 200:
                    os.system('python kill_process.py')
                    print('--------------------重新运行程序-----------------------')
                    os.system("gnome-terminal -e 'bash -c \"python {}\"'".format(args.path))
        except requests.exceptions.ConnectionError:
            print('--------------------该程序未运行，开始运行该程序-----------------------')
            os.system("gnome-terminal -e 'bash -c \"python {}\"'".format(args.path))
        # time.sleep(2)
        time.sleep(gap_minute * 60)
