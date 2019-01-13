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
from multiprocessing import Pool
from progressbar import ProgressBar
from multiprocessing import cpu_count
from sqlalchemy.exc import InternalError
from requests.exceptions import ConnectionError

import sys
sys.path.append('..')
sys.setrecursionlimit(1000000)

import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

import ip_pool
from utils import utils
from utils import sql_utils
from crawler import Crawler

LOG_ID = 'CRAWLER_NEWS'

class news_crawler(Crawler):
    def __init__(self):
        self.config = utils.CONF()
        self.agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        self.headers = {'User-Agent': self.agent}
        self.cpu_num = cpu_count()
        self.proxy_list = []


    def _get_html(self, url, encoding):
        # utils.LOG('i', LOG_ID, url)
        if len(self.proxy_list) < 50:
            self.proxy_list = self.get_proxy()
        other_encoding = {
            'utf-8': 'gbk',
            'gbk': 'utf-8'
        }[encoding]
        final_encoding = ''
        loop_count = 0
        while True:
            current_proxy = random.sample(self.proxy_list, 1)[0]
            current_proxy_dict = {
                'http': 'http://' + current_proxy,
                'https': 'https://' + current_proxy 
            }
            # self.check_proxy(current_proxy)
            try:
                req = requests.get(url, headers=self.headers, proxies=current_proxy_dict, timeout = 500)
                # req = requests.get(url, headers=self.headers, timeout = 500)
                break
            except Exception as e:
                pass
            loop_count = loop_count + 1
            if loop_count > 30:
                utils.LOG('i', LOG_ID, '循环30次后读取网页失败')
                break
        
        if req.encoding == None:
            req_encoding = 'utf-8'
        else:
            req_encoding = req.encoding
        if req.status_code != 404:
            # encode in ISO-8859-1, and change it into gbk encoding
            try:
                html_content = req.text.encode(req_encoding).decode(encoding)
            # 处理编码问题
            except UnicodeDecodeError as e:
                try:
                    html_content = req.text.encode(req_encoding).decode(other_encoding)
                except UnicodeDecodeError as e:
                    pass
                    try:
                        html_content = req.text.encode(req_encoding).decode('latin-1')
                    except UnicodeDecodeError as e:
                        pass
            
            return html_content
        else:
            utils.LOG('e', LOG_ID, 'Page Not Found')
            return '404'


    def get_cd_content(self, url):  # china daily news content
        # http://www.chinadaily.com.cn/a/201901/11/WS5c38b543a3106c65c34e3feb.html
        url = 'http:' + url
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
        content_text = ' '.join(content_list)
        return content_text

    def get_cd_list(self):
        ip_pool.ip_pool('china_daily')
        self.proxy_list = self.get_proxy()
        utils.LOG(LOG_ID, '共有{}个IP可供爬虫使用'.format(len(self.proxy_list)))
        saved_pages = sql_utils.select('select distinct(page) as page from news where media="china_daily" ')['page'].values.tolist()  # 已经保存的页面
        all_pages = list(range(1, 114))  # 新闻列表共有113页
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
            utils.LOG('i', LOG_ID, '开始解析网页')
            html_content = self._get_html(news_list_url, encoding='gbk')
            html_content = html_content.replace('<EM>', '').replace('</EM>', '')  # 去除斜体
            re_content = r'''<h4><a shape="rect" href="(.*?)">(.*?)</a></h4>\n\s*<b>(.*?)</b>'''
            pattern = re.compile(re_content, re.DOTALL)
            a = re.findall(pattern, html_content)
            utils.LOG('i', LOG_ID, '网页解析结束，本页共有{}条新闻'.format(len(a)))
            b = ProgressBar()
            for i in b(a):
                content_url = i[0]
                link_list.append(content_url)
                time_ = i[-1].split(' ')
                time_list.append(time_[1])
                date_list.append(time_[0])
                title_list.append(i[1])
                content_list.append(self.get_cd_content(content_url))
            
            pd_cd_news = pd.DataFrame(columns=['date', 'time', 'title', 'content', 'link', 'media', 'language', 'page'])
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
            except Exception as e:
                utils.LOG('w', LOG_ID, 'SHIT HAPPEND IN SAVING PROGRESS!')
                # sql_utils.replace_save(pd_cd_news, 'news')
                pd_cd_news.to_csv('./china_daily_{}'.format(page), index=False)

            end_time = time.time()
            used_time = end_time - start_time
            utils.LOG('i', LOG_ID, 'Used {:4f} seconds in crawling {}th page from china daily'.format(used_time, page))

    def get_rmw_content(self, url):  # 人民网新闻内容
        base_url = 'http://usa.people.com.cn'
        url = base_url + url
        html_content = self._get_html(url, encoding='gbk')
        # 获取新闻时间
        re_content = r'''日\d{1,2}:\d{1,2}&nbsp;&nbsp;'''  # 获取新闻时间
        pattern = re.compile(re_content, re.DOTALL)
        a = re.findall(pattern, html_content)
        time_ = a[0][1:6]
        
        div_content = BeautifulSoup(html_content, 'lxml')
        content_list = []
        content_div = div_content.find('div', class_='clearfix w1000_320 text_con').find('div', class_='fl text_con_left').find('div', class_='box_con')
        if content_div:
            content_p = content_div.find_all('p')
            if content_p:
                for p in content_div.find_all('p'):
                    content_list.append(p.get_text())
            else:
                utils.LOG('w', LOG_ID, '无新闻p')
        else:
            utils.LOG('w', LOG_ID, '无新闻div')
        content_text = ' '.join(content_list).replace('"', '')
        return time_, content_text

    def get_rmw_list(self):  # 人民网新闻内容
        ip_pool.ip_pool('renminwang')
        self.proxy_list = self.get_proxy()
        utils.LOG(LOG_ID, '共有{}个IP可供爬虫使用'.format(len(self.proxy_list)))
        base_url = 'http://usa.people.com.cn'
        saved_pages = sql_utils.select('select distinct(page) as page from news where media="renminwang"')['page'].values.tolist()  # 已经保存的页面
        all_pages = list(range(1, 8))  # 新闻列表共有7页
        left_pages = list(set(saved_pages) ^ set(all_pages))[:1]
        # utils.LOG('i', LOG_ID, left_pages)
        utils.LOG('i', LOG_ID, 'There are still {} pages in renminwang'.format(len(left_pages)))
        for page in left_pages:
            start_time = time.time()
            news_list_url = 'http://usa.people.com.cn/GB/406587/index{}.html'.format(page)
            utils.LOG('i', LOG_ID, 'Start crawling {}th page from renminwang'.format(page))
            date_list = []
            time_list = []
            title_list = []
            content_list = []
            link_list = []
            utils.LOG('i', LOG_ID, '开始解析网页')
            html_content = self._get_html(news_list_url, encoding='gbk')
            re_content = r'''<li><a href='(.*?)' target=_blank>(.*?)</a> <em>(.*?)</em></li>'''
            pattern = re.compile(re_content, re.DOTALL)
            a = re.findall(pattern, html_content)
            utils.LOG('i', LOG_ID, '网页解析结束, 该网页共有{}条新闻'.format(len(a)))
            b = ProgressBar()
            for i in b(a):
                date_list.append(i[-1])
                title_list.append(i[1])
                link = i[0]
                link_list.append(link)
                time_, content = self.get_rmw_content(link)
                # time_ , content = '00:00', 'no content'
                time_list.append(time_)
                content_list.append(content)
            
            pd_cd_news = pd.DataFrame(columns=['date', 'time', 'title', 'content', 'link', 'media', 'language', 'page'])
            pd_cd_news['date'] = date_list
            pd_cd_news['time'] = time_list
            pd_cd_news['title'] = title_list
            pd_cd_news['content'] = content_list
            pd_cd_news['link'] = link_list
            pd_cd_news['media'] = 'renminwang'
            pd_cd_news['language'] = 'chinese'
            pd_cd_news['page'] = page

            try:
                sql_utils.save(pd_cd_news, 'news')
            except Exception as e:
                utils.LOG('w', LOG_ID, 'SHIT HAPPEND IN SAVING PROGRESS!')
                # sql_utils.replace_save(pd_cd_news, 'news')
                pd_cd_news.to_csv('./renminwang_{}'.format(page), index=False)

            end_time = time.time()
            used_time = end_time - start_time
            utils.LOG('i', LOG_ID, 'Used {:4f} seconds in crawling {}th page from renminwang'.format(used_time, page))
                


            


if __name__ == "__main__":
    crawler = news_crawler()
    # utils.LOG('i', LOG_ID, crawler._get_html('http://usa.people.com.cn/GB/406587/index7.html', encoding='utf-8'))  # 人民网新闻列表
    # utils.LOG('i', LOG_ID, crawler._get_html('http://www.chinadaily.com.cn/world/china-us/page_1.html', encoding='gbk'))

    # utils.LOG('i', LOG_ID, crawler.get_cd_content('//www.chinadaily.com.cn/a/201901/11/WS5c38b543a3106c65c34e3feb.html'))  # china daily 新闻内容
    # utils.LOG('i', LOG_ID, crawler.get_rmw_content('/n1/2018/0525/c241376-30014901.html'))
    # crawler.get_cd_list()
    crawler.get_rmw_list()





