import os
import argparse
import logging


parser = argparse.ArgumentParser()
parser.add_argument('-user', type=str, default="mod", help='killed process who run on the server')
args = parser.parse_args()


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s  %(levelname)s  %(message)s  %(lineno)d",
                    filename='kill.log')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('--------start to kill process---------')
    out_list = os.popen('nvidia-smi').readlines()
    user = args.user.strip()
    keyword = 'cwd ->'

    for line in os.popen('nvidia-smi').readlines():
        if 'python' in line:
            pid = line.split()[4]
            detail_execute = 'ls -l /proc/' + pid
            details = os.popen(detail_execute).readlines()
            for detail in details:
                if user in detail and keyword in detail:
                    kill_execute = 'kill -9 ' + pid
                    os.system(kill_execute)
                    print('--------killed the process ' + pid + '----------')
                    logging.info('  kill the process ' + pid + '  ')
                    break
            break
