# -*- coding: utf-8 -*-

import yaml
import os
import time
from datetime import datetime, timedelta
import logging


def CONF():
    config = yaml.load(open('../config/config.yml'))
    return config


def get_platform():
    return 'windows' if os.name=='nt' else 'macos'


def get_sql_config():
    config = yaml.load(open('../config/sql_config.yml'))
    return config['windows_sql']


def get_time():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


# log util
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    # filename=os.path.join(CONF()['log_dir'], 'log_{}.log'.format(
    #     time.strftime('%Y%m%d%H%M%S'))),
    # filemode='w'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(message)s')

console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

class LogManager:
    def __init__(self):
        self.total_error = 0
        self.total_warning = 0
        self.total_info = 0
        self.id_cnt = {}
        self.id_msg = {}

    def inc(self, log_id):
        if log_id not in self.id_cnt:
            self.id_cnt[log_id] = 0
        self.id_cnt[log_id] += 1


logger_ = LogManager()


def LOG(log_type='i', log_id='SYS-000', msg=''):
    # logger_.inc(log_id)
    if log_type == 'e':
        logging.error('{}  {}'.format(log_id, msg))
        # logger_.total_error += 1
    elif log_type == 'w':
        logging.warning('{}  {}'.format(log_id, msg))
        # logger_.total_warning += 1
    else:
        logging.info('{}  {}'.format(log_id, msg))
        # logger_.total_info += 1


if __name__ == '__main__':
    test()

