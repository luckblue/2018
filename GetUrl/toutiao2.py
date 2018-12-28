import requests
import re,json,os
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
#引入模块config中所有变量
#from config import *
import pymongo
from hashlib import md5
from multiprocessing import Pool

def get_page_index(offset, keyword):
    #获取页面的html
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3,
        'from': 'gallery'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

#解析索引页
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

#获取详情页的html
def get_page_detail(url):
    try:
        headers = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.162Safari / 537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错', url)
        return None

#解析详情页
def parse_page_detail(html):
    #获取详情页的标题和图片url
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)

    #利用正则提取图片地址
    images_pattern = re.compile('.*?gallery: JSON.parse\("(.*?)\"\)', re.S)
    result = re.search(images_pattern, html)
    if result:
        data = json.loads(result.group(1).replace('\\',''))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            #提取图片
            images = [item.get('url') for item in sub_images]
            #保存图片到本地
            for image in images: download_image(image)
            return {
                'title': title,
                'image': images
            }

#保存图片
def save_image(result):
    file_path = 'Z:\\test'.format(os.getcwd(), md5(result).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(result)

#下载图片
def download_image(url):
    try:
        print('正在下载',url)
        r = requests.get(url)
        if r.status_code == 200:
            save_image(r.content)
        return False
    except RequestException:
        print('请求图片出错')
        return False

#开启多线程抓取
def main(offset):
    html = get_page_index(offset,'街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html)
            #save_to_mongo(result)

if __name__ == '__main__':
    pool = Pool()
    group = [x * 20 for x in range(1,21)]
    pool.map(main,group)
    pool.close()
    main()

