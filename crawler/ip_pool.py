# -*- coding: utf-8 -*-

import requests
import time
import random
import os
import re
from bs4 import BeautifulSoup
import pandas as pd
import pickle
import multiprocessing as mp
from multiprocessing import Pool
from multiprocessing import cpu_count
from requests.exceptions import ProxyError, ConnectTimeout, SSLError, ReadTimeout
from pymysql.err import OperationalError

import sys
sys.path.append('..')

from utils import utils
from utils import sql_utils
from crawler import Crawler

LOG_ID = 'CRAWLER_IP_POOL'

class ip_pool(Crawler):
    """
    maintain an ip pool for data crawler
    use http://www.xicidaili.com/
    """
    def __init__(self, media):
        sql_utils.execute('delete from ip_pool')
        self.config = utils.CONF()
        self.agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        self.headers = {'User-Agent': self.agent}
        self.start_time = utils.get_time()
        self.need_pages = 3
        self.proxy_list = self.get_proxy(pro_type='HTTP')
        self.urls = [self.config['ip_link']['xici_hide'], self.config['ip_link']['xici_norm']]
        self.url_type = ''

        self.test_url = {
            'china_daily': 'http://www.chinadaily.com.cn/',
            'renminwang': 'http://usa.people.com.cn/GB/406587/'
        }[media]
        self.get_ip()


    def get_ip(self):
        # sql_utils.execute('delete from ip_pool')
        for url in self.urls:
            self.url_type = self._url_type(url)
            start_page = 0
            pages = [str(i) for i in list(range(start_page, self.need_pages))]
            if start_page == 0:
                pages[0] = ''  # first  page don't have path
            ip_pool = []
            for page in pages:
                html_content = self._get_html(url + page)
                self._parse_hide_html(html_content)
            time.sleep(random.random() * 20)

    def _get_html(self, url):
        utils.LOG(LOG_ID, 'get html from {}'.format(url))
        if len(self.proxy_list) > 0:
            current_proxy = random.sample(self.proxy_list, 1)[0]
            current_proxy_dict = {
                'HTTP': 'http://' + current_proxy,
                'HTTPS': 'https://'+ current_proxy
            }
            req = requests.get(url, headers=self.headers, proxies=current_proxy_dict, timeout = 500)
        else:
            req = requests.get(url, headers=self.headers, timeout = 500)
        html_content = req.text
        return html_content
        
    def _url_type(self ,url):
        # 判断爬取的IP类别： 高匿(hide)/透明(norm)
        if url.endswith('/nn/'):
            return 'hide'
        elif url.endswith('/nt/'):
            return 'norm'
        else:
            return 'other'
        
    def _parse_hide_html(self, html_content):
        soup = BeautifulSoup(html_content, "lxml")
        table = soup.find('table', id="ip_list")
        pool = Pool(cpu_count())
        ips = []
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            tmp = []
            for item in cells:
                tmp.append(item)
            if len(tmp) > 0:
                claim_time_item = float(tmp[6].find("div", class_="bar").attrs['title'].replace('秒', ''))
                ips.append([tmp[1].get_text(), tmp[2].get_text(), tmp[5].get_text(), claim_time_item])
        ip_list = []
        port_list = []
        claim_time_list = []
        test_time_list = []
        type_list = []
        mp_result_list = []  # 多线程运行结果

        for ip in ips:
            pro_type = ip[2]
            if pro_type in ['HTTP', 'HTTPS']:  # 过滤socks类型IP
                test_proxy = ip[0] + ':' + ip[1]
            
                ip_list.append(ip[0])
                port_list.append(ip[1])
                type_list.append(pro_type)
                mp_result_list.append(pool.apply_async(self.test_proxy, (test_proxy, pro_type, )))
                claim_time_list.append(ip[3])
        pool.close()
        pool.join()

        for res in mp_result_list:
            test_result = res.get()
            if test_result[0]:
                test_time_list.append(test_result[-1])
            else:
                test_time_list.append(100.0)

        ip_pool = pd.DataFrame(columns=['ip', 'port', 'claim_time', 'test_time', 'pro_type', 'net_type'])
        ip_pool['ip'] = ip_list
        ip_pool['port'] = port_list
        ip_pool['claim_time'] = claim_time_list
        ip_pool['test_time'] = test_time_list
        ip_pool['pro_type'] = type_list
        ip_pool['net_type'] = self.url_type
        try:
            sql_utils.save(ip_pool, 'ip_pool', if_exists='append')
        except Exception as e:
            sql_utils.replace_save(ip_pool, 'ip_pool')

    def test_proxy(self, proxy, pro_type):
        test_url = self.test_url
        timeout = 50
        try:
            proxies = {
                'https': 'https://' + proxy,
                'http': 'http://' + proxy
            }
            starttime = time.time()
            requests.get(test_url, timeout=timeout, proxies=proxies)
            endtime = time.time()
            used_time = endtime - starttime
            utils.LOG('i', LOG_ID, '{} valid, Used Time: {:.4f}'.format(proxies, used_time))
            return True, used_time
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            utils.LOG('e', LOG_ID, 'Proxy Invalid: {}'.format(proxy))
            return False, None

    def is_crawl_ip(self):
        if sql_utils.if_table_exists('ip_pool'):
            with open('./crawl_time.pkl', 'wb') as output:
                pickle.dump(self.start_time, output)
            utils.LOG(LOG_ID, 'crawl ips from xicidaili')
            return True
        else:
            crawl_time = ''
            with open('./crawl_time.pkl', 'rb') as input:
                crawl_time = pickle.load(input)
            crawl_time_num = time.strptime(crawl_time, '%Y%m%d%H%M%S')
            now_time = time.localtime(time.time())
            if (now_time - crawl_time_num).hours + 13 < 12:
                return False
            else:
                utils.LOG(LOG_ID, 'ips are too old, updating...')
                with open('./crawl_time.pkl', 'wb') as output:
                    pickle.dump(utils.get_time(), output)
                return True


if __name__ == '__main__':
    crawler = ip_pool()
    crawler.get_ip()

    