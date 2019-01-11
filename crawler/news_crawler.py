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
        if len(self.proxy_list) < 50:
            self.proxy_list = self.get_proxy()
        other_encoding = {
            'utf-8': 'gbk',
            'gbk': 'utf-8'
        }[encoding]
        final_encoding = ''
        
        current_proxy = random.sample(self.proxy_list, 1)[0]
        utils.LOG(LOG_ID, 'get html from {} in {}'.format(url, current_proxy))
        current_proxy_dict = {
            'HTTP': 'http://' + current_proxy,
            'HTTPS': 'https://' + current_proxy 
        }
        try:
            # req = requests.get(url, headers=self.headers, proxies=current_proxy_dict, timeout = 500)
            req = requests.get(url, headers=self.headers, timeout = 500)
        except Exception as e:
            new_proxy = random.sample(self.proxy_list, 1)[0]
            current_proxy_dict = {
                'HTTP': 'http://' + new_proxy,
                'HTTPS': 'https://' + new_proxy 
            }
            try:  # 尝试第二次
                # req = requests.get(url, headers=self.headers, proxies=current_proxy_dict, timeout = 500)
                req = requests.get(url, headers=self.headers, proxies=current_proxy_dict, timeout = 500)
                self.proxy_list.remove(current_proxy)
            except Exception as e:
                utils.LOG('e', LOG_ID, 'failed to connect {}'.format(url))
                return 'break'
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
                        pd_fail_url = pd.DataFrame(columns=['url'])
                        pd_fail_url['url'] = [url]
                        utils.LOG('w', LOG_ID, url)
                        self.fail_url_list.append(pd_fail_url)

            return html_content
        else:
            utils.LOG('e', LOG_ID, 'Page Not Found')
            return '404'


    def _get_content(self, url):
        html_content = self._get_html(url, encoding='gbk', mode='article')
        div_content = BeautifulSoup(html_content, 'lxml')
        content_list = []
        content_div = div_content.find('div', class_='stockcodec .xeditor')
        if not content_div:
            content_div = div_content.find('div', class_='xeditor_content')
        if content_div:
            content_p = content_div.find_all('p')
            if content_p:
                for p in content_div.find_all('p'):
                    content_list.append(p.get_text().replace('\n', '').replace(' ', ''))
                return ''.join(content_list)
            else:
                return content_div.get_text().replace('\n', '').replace(' ', '')
        else:
            utils.LOG('w', LOG_ID, '******* content failed *******')
            return 'no result'

    def _parse_list(self, even_div):
        read_num = int(even_div.find('span', class_='l1').get_text())
        comment_num = int(even_div.find('span', class_='l2').get_text())
        title_div = even_div.find('span', class_='l3').find_all('a')[-1]  # 问董秘出现时，多一个a标签
        link = self.link[:-1] + title_div.attrs['href']
        content = self._get_content(link).replace('\r', '')
        title = title_div.string
        author_div = even_div.find('span', class_='l4').a
        if author_div:
            author = author_div.string
        else:
            author = ''
        publish = even_div.find('span', class_='l6').get_text()
        update = even_div.find('span', class_='l5').get_text()
        return 'MAGA'.join([str(i) for i in [read_num, comment_num, link, content, title, author, publish, update]])

    def _get_comment_from_page(self, page):
        start_time = time.time()
        pd_comment = pd.DataFrame(columns=['publish_time', 'update_time', 'read_num', 'comment_num', 'link', 'title', 'content', 'page', 'stock'])
        publish_list = []
        update_list = []
        read_list = []
        comment_list = []
        link_list = []
        title_list = []
        content_list = []
        author_list = []

        target_link = self.link + 'list,{}.html'.format(page)
        target_html = self._get_html(target_link, encoding='utf-8')
        soup = BeautifulSoup(target_html, "lxml")
        content_div = soup.find('div', id='articlelistnew')
        if content_div:
            # even_list_div = content_div.find_all('div', class_='articleh normal_post')
            even_list_div = content_div.find_all('div', attrs={"class":re.compile(r"articleh normal_post(\s\w+)?")})
            for even_div in even_list_div:
                record = self._parse_list(even_div)
                record = record.split('MAGA')
                publish_list.append(record[6])
                update_list.append(record[7])
                read_list.append(record[0])
                comment_list.append(record[1])
                link_list.append(record[2])
                title_list.append(record[4])
                content_list.append(record[3])
                author_list.append(record[5])

            pd_comment['publish_time'] = publish_list
            pd_comment['update_time'] = update_list
            pd_comment['read_num'] = read_list
            pd_comment['comment_num'] = comment_list
            pd_comment['link'] = link_list
            pd_comment['title'] = title_list
            pd_comment['content'] = content_list
            pd_comment['author'] = author_list
            stock_page = page.split('_')
            pd_comment['page'] = stock_page[1]
            pd_comment['stock'] = stock_page[0]

            pd_comment['page'] = pd_comment['page'].astype(int)
            pd_comment['comment_num'] = pd_comment['comment_num'].astype(int)
            pd_comment['read_num'] = pd_comment['read_num'].astype(int)
        
            try:
                sql_utils.save(pd_comment, 'eastmoney_sentiments', if_exists='append')
            except InternalError as e:
                pd_comment.to_csv('./fail_saved_news/eastmoney_{}.csv'.format(page), index=False, encoding='utf-8')
                utils.LOG('w', LOG_ID, '####### ERROR !!! ########')

            end_time = time.time()
            used_time = end_time - start_time
            utils.LOG('i', LOG_ID, 'use {:4} senconds in {}\'s page useing no.{} core'.format(used_time, page, os.getpid()))
        else:
            utils.LOG('w', LOG_ID, '******* page {} 未能爬取成功 *******'.format(page))

    def get_comments(self):
        pd_pages = sql_utils.select('select stock, page from eastmoney_pages')
        stock_list = pd_pages['stock'].values.tolist()
        page_list = pd_pages['page'].values.tolist()
        all_pages = []

        for i in range(len(stock_list)):
            for j in range(page_list[i]):
                all_pages.append('{}_{}'.format(stock_list[i], (j+1)))

        for page in self.saved_stock:
            all_pages.remove(page)  # 删除已经存储的数据


        utils.LOG('i', LOG_ID, '####### 已保存{}个页面，剩余共需爬取{}个页面 #######'.format(len(self.saved_stock), len(all_pages)))

        pool = Pool(self.cpu_num)
        pool.map(self._get_comment_from_page, all_pages[:10000])
        pool.close()
        pool.join()

                

    def _get_max_page(self, stock, saved_page):  # 获取每只个股的最大值
        utils.LOG('i', LOG_ID, 'FIND {}\'s MAX PAGE'.format(stock))
        max_num = 0
        start_page = saved_page
        for i in range(saved_page, 100000):
            target_link = self.link + 'list,{}_{}.html'.format(stock, i)
            target_html = self._get_html(target_link, encoding='gbk', mode='article')
            soup = BeautifulSoup(target_html, "lxml")
            content_div = soup.find('div', id='articlelistnew')
            if not content_div:
                max_num = i
                break
            if content_div.find('div', class_='noarticle'):  # 该股票无后续页面
                max_num = i
                break       
            max_num = i
        max_num = max_num - 1
        return max_num
                    
    def get_stock_page(self):
        pd_saved_page = sql_utils.select('select stock, page from eastmoney_sentiments')
        stock_list = pd_saved_page['stock'].values.tolist()
        page_list = pd_saved_page['page'].values.tolist()

        pd_pages = pd.DataFrame(columns=['stock', 'page'])
        stock_list = []
        page_list = []
        
        pool = Pool(self.cpu_num)
        mp_list = []
        for i in range(len(self.code_list)):
            if self.code_list[i] in stock_list:
                saved_page = page_list[i]
            else:
                saved_page = 1
            stock_list.append(self.code_list[i])
            mp_list.append(pool.apply_async(self._get_max_page, (stock_list[i], saved_page, )))
        
        for mp_r in mp_list:
            page_list.append(mp_r.get())

        pd_pages['stock'] = stock_list
        pd_pages['page'] = page_list
        sql_utils.save(pd_pages, 'eastmoney_pages', if_exists='append')

    def _get_codes(self):
        pd_stock_basic = sql_utils.select("select * from stock_basic where exchange='SSE'")
        stock_list = pd_stock_basic['symbol'].values.tolist()
        return stock_list

    def _get_saved_codes_disuse(self):
        pd_saved = sql_utils.select("select stock, page from eastmoney_sentiments")
        pd_saved_dict = dict(list(pd_saved.groupby(['stock'])))
        saved_keys = pd_saved_dict.keys()
        saved_dict = {}
        for saved_key in saved_keys:
            saved_dict[saved_key] = max(pd_saved_dict[saved_key]['page'].values.tolist())
        return saved_dict
        
    def _get_saved_codes(self):
        pd_saved = sql_utils.select("select stock, page from eastmoney_sentiments")
        pd_saved['page'] = pd_saved['page'].astype(str)
        pd_saved['label'] = pd_saved['stock'] + '_' + pd_saved['page']
        return list(set(pd_saved['label'].values.tolist()))


if __name__ == "__main__":
    crawler = news_crawler()
    utils.LOG('i', LOG_ID, crawler._get_html('http://usa.people.com.cn/GB/406587/index7.html', encoding='utf-8'))




