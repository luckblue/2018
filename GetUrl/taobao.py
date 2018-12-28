import os
import sys
import requests
import re
import json
import time
import random

from bs4 import BeautifulSoup
from urllib.parse import urlencode
from requests.exceptions import RequestException

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir)


def get_proxy():
    r = requests.get('http://127.0.0.1:5000/get')
    proxy = BeautifulSoup(r.text, "lxml").get_text()
    return proxy


def crawl(url, proxy):
    proxies = {'http': proxy}
    try:  # 防止程序中断
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:  # 如果访问成功则返回文本内容
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None


def main():

    # 抓取的网页url
    default_url = 'https://rate.tmall.com/list_detail_rate.htm?'

    # 指定保存路径
    f = open('D:\\test.csv', 'w', encoding='gb18030')  # csv文件编码只能'gbk'
    f.write('买家评论, 评论时间, 追加评论, 追加评论日期, 追加天数, 昵称\n')

    # 获取代理IP
    proxy = get_proxy()
    print(proxy)

    # 循环抓取每一页评论
    i = 1
    while 1:
        # 构造url的过程，get请求的参数
        pagram = {
            'sellerId': '1055542410',
            'itemId': '546577440744',
            'currentPage': i
        }

        # 随机休眠，行为分析，防止访问过快，避免被网站检测封IP
        # time.sleep(random.random()*10)
        time.sleep(5)

        # 请求评论的URL
        url = default_url + urlencode(pagram)
        print('正在下载第%s页数据' % i)

        # 使用代理请求评论数据
        data = crawl(url, proxy)
        # 请求无效，更换代理IP重新请求
        while data==None:
            print('请求失败，重新获取代理IP，重新请求！')
            proxy = get_proxy()
            print(proxy)
            data = crawl(url, proxy)
            time.sleep(10)

        # 解析数据
        data = re.findall(r'{.*}', data)[0]
        # json数据->字典
        data = json.loads(data)
        data = data['rateDetail']['rateList']

        if data:
            # 保存数据
            for item in data:
                if item['appendComment']:
                    f.write('%s,%s,%s,%s,%s,%s\n'%(
                        item['rateContent'],
                        item['rateDate'],
                        item['appendComment']['content'],
                        item['appendComment']['commentTime'],
                        item['appendComment']['days'],
                        item['displayUserNick']
                    ))
                else:
                    f.write('%s,%s,%s,%s,%s,%s\n' % (
                        item['rateContent'],
                        item['rateDate'],
                        '',
                        '',
                        '',
                        item['displayUserNick']
                    ))
            i += 1
        else:
            break

    print('下载完成！')

if __name__ == '__main__':
    main()