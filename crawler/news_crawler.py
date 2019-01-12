# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import time
import random
import datetime
import requests
import pickle
import re
import os
from bs4 import BeautifulSoup
import multiprocessing as mp
from progressbar import ProgressBar
from multiprocessing import Pool
from multiprocessing import cpu_count
from sqlalchemy.exc import InternalError
from requests.exceptions import ConnectionError

import sys
sys.path.append('..')
sys.setrecursionlimit(1000000)

import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

from ip_pool import ip_pool
from utils import utils
from utils import sql_utils
from crawler import Crawler

LOG_ID = 'CRAWLER_NEWS'

class news_crawler(Crawler):
    def __init__(self):
        self.config = utils.CONF()
        self.agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        self.headers = {'User-Agent': self.agent}
        # self.link = self.config['east_money']
        self.cpu_num = cpu_count()
        # self.code_list = self._get_codes()
        # self.saved_stock = self._get_saved_codes()
        self.proxy_list = self.get_proxy()
        if len(self.proxy_list) < 50:
            self.proxy_list = self.get_proxy()
        self.proxy_list_len = len(self.proxy_list)
        self.current_proxy_index = random.randint(0, self.proxy_list_len-1)
        utils.LOG(LOG_ID, '共有{}个IP可供爬虫使用'.format(self.proxy_list_len))

    def _get_html(self, url, encoding):
        print(url)
        if len(self.proxy_list) < 50:
            self.proxy_list = self.get_proxy()
        other_encoding = {
            'utf-8': 'gbk',
            'gbk': 'utf-8'
        }[encoding]
        final_encoding = ''
        
        while True:
            loop_count = 0
            current_proxy = random.sample(self.proxy_list, 1)[0]
            current_proxy_dict = {
                'http': 'http://' + current_proxy,
                'https': 'https://' + current_proxy 
            }
            # self.check_proxy(current_proxy)
            try:
                req = requests.get(url, headers=self.headers, proxies=current_proxy_dict, timeout = 500)
                break
            except Exception as e:
                # self.proxy_list.remove(current_proxy)
                pass
            loop_count = loop_count + 1
            if loop_count > 30:
                break

        if req.status_code != 404:
            # encode in ISO-8859-1, and change it into gbk encoding
            try:
                html_content = req.text.encode(req.encoding).decode(encoding)
            # 处理编码问题
            except UnicodeDecodeError as e:
                try:
                    html_content = req.text.encode(req.encoding).decode(other_encoding)
                except UnicodeDecodeError as e:
                    pass
                    try:
                        html_content = req.text.encode(req.encoding).decode('latin-1')
                    except UnicodeDecodeError as e:
                        pass
            html_content = html_content.replace('<EM>', '').replace('</EM>', '')  # 去除斜体
            return html_content
        else:
            utils.LOG('e', LOG_ID, 'Page Not Found')
            return '404'


    def get_cd_content(self, url):  # china daily news content
        # http://www.chinadaily.com.cn/a/201901/11/WS5c38b543a3106c65c34e3feb.html
        url = 'http:' + url
        print(url)
        html_content = self._get_html(url, encoding='utf-8')
        div_content = BeautifulSoup(html_content, 'lxml')
        content_list = []
        content_div = div_content.find('div', id='Content')
        if content_div:
            content_p = content_div.find_all('p')
            if content_p:
                for p in content_div.find_all('p'):
                    content_list.append(p.get_text().replace('"', '').replace('\xa0', ''))
            else:
                utils.LOG('w', LOG_ID, '无新闻p')
        else:
            utils.LOG('w', LOG_ID, '无新闻div')
        return ' '.join(content_list)

    def get_cd_list(self):
        saved_pages = sql_utils.select('select distinct(page) from news ').values.tolist()  # 已经保存的页面
        all_pages = list(range(1, 113))
        left_pages = list(set(saved_pages) ^ set(all_pages))
        utils.LOG('i', LOG_ID, 'There are still {} pages in china daily'.format(len(left_pages)))
        for page in left_pages:
            start_time = time.time()
            news_list_url = 'http://www.chinadaily.com.cn/world/china-us/page_{}.html'.format(page)
            utils.LOG('i', LOG_ID, 'Start crawling {}th page from china daily'.format(page))
            date_list = []
            time_list = []
            title_list = []
            content_list = []
            link_list = []
            html_content = self._get_html(news_list_url, encoding='gbk')
            re_content = r'''<h4><a shape="rect" href="(.*?)">(.*?)</a></h4>\n\s*<b>(.*?)</b>'''
            pattern = re.compile(re_content, re.DOTALL)
            a = re.findall(pattern, html_content)
            for i in a:
                print(i)
                content_url = i[0]
                if not content_url.startswith('http'):
                    content_url = 'http:' + content_url
                link_list.append(content_url)
                time_ = i[-1].split(' ')
                time_list.append(time_[1])
                date_list.append(time_[0])
                title_list.append(i[1])
                content_list.append(self.get_cd_content(content_url))
            
            pd_cd_news = pd.DataFrame(columns=['date', 'time', 'title', 'content', 'link', 'media', 'language', 'label'])
            pd_cd_news['date'] = date_list
            pd_cd_news['time'] = time_list
            pd_cd_news['title'] = title_list
            pd_cd_news['content'] = content_list
            pd_cd_news['link'] = link_list
            pd_cd_news['media'] = 'china_daily'
            pd_cd_news['language'] = 'english'
            pd_cd_news['page'] = page

            try:
                sql_utils.save(pd_cd_news, 'news')
            except:
                utils.LOG('w', LOG_ID, 'SHIT HAPPEND IN SAVING PROGRESS!')
                sql_utils.replace_save(pd_cd_news, 'news')

            end_time = time.time()
            used_time = end_time - start_time
            utils.LOG('i', LOG_ID, 'Used {:4f} seconds in crawling {}th page from china daily')

    def get_rmw_content(self, url):  # 人民网新闻内容
        pass


if __name__ == "__main__":
    crawler = news_crawler()
    # utils.LOG('i', LOG_ID, crawler._get_html('http://usa.people.com.cn/GB/406587/index7.html', encoding='utf-8'))  # 人民网新闻列表
    # utils.LOG('i', LOG_ID, crawler._get_html('http://www.chinadaily.com.cn/world/china-us/page_1.html', encoding='gbk'))

    # utils.LOG('i', LOG_ID, crawler.get_cd_content('//www.chinadaily.com.cn/a/201901/11/WS5c38b543a3106c65c34e3feb.html'))  # china daily 新闻内容
    crawler.get_cd_list()





