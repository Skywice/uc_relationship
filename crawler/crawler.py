# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import time
import random
import requests
import os
import re

from requests.exceptions import ProxyError, ConnectTimeout, SSLError, ReadTimeout
from pymysql.err import OperationalError

import sys
sys.path.append('..')

from utils import utils
from utils import sql_utils

LOG_ID = 'CRAWLER'

class Crawler(object):
    def test_proxy(self, proxy):
        test_url = 'https://www.baidu.com/'
        timeout = 15
        print(os.getpid())
        try:
            proxies = {
                'https': 'http://' + proxy
            }
            starttime = time.time()
            requests.get(test_url, timeout=timeout, proxies=proxies)
            endtime = time.time()
            used_time = endtime - starttime
            utils.LOG(LOG_ID, '{} valid, Used Time: {:.4f}'.format(proxies, used_time))
            return True, used_time
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            utils.LOG('e', LOG_ID, 'Proxy Invalid: {}'.format(proxy))
            return False, None

    def get_proxy(self, pro_type='HTTP'):
        df_proxy = sql_utils.select('select * from ip_pool where pro_type = "{}" and test_time < 100'.format(pro_type))
        df_proxy['proxy'] = df_proxy['ip'] + ':' + df_proxy['port']
        proxy_list = df_proxy['proxy'].values.tolist()
        return proxy_list

    def check_proxy(self, proxy=''):
        # chekc_url = 'https://www.whatismyip.com/'
        chekc_url = 'http://icanhazip.com/'
        if proxy == '':
            req = requests.get(chekc_url, headers=self.headers, timeout=500)
        else:
            proxies = {
                'HTTP': 'http://' + proxy,
                'HTTPS': 'https://' + proxy
            }
            req = requests.get(chekc_url, headers=self.headers, timeout=500, proxies=proxies)
        html_content = req.text
        response_ip = html_content
        input_ip = proxy.split(':')[0]
        utils.LOG('i', LOG_ID, 'the input ip is {} and the response ip is {}'.format(input_ip, response_ip))
        if input_ip == response_ip:
            return True
        else:
            return False


    