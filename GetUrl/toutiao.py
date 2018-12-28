import json
import os
import re
from hashlib import md5
from multiprocessing import Pool

from urllib.parse import urlencode
#import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

#from ToutiaoJiepai.config import *


GROUP_START = 1
GROUP_END = 1
KEYWORD = '街拍'

def get_page_index(offset, keyword):
    """抓取索引页的内容"""
    data = {  # 请求参数，offset和keyword我们设置成变量，方便改变。
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery'
    }
    # urlencode()可以把字典对象转化为url的请求参数
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:  # 防止程序中断
        response = requests.get(url)
        if response.status_code == 200:  # 如果访问成功则返回文本内容
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def parse_page_index(html):
    """ 解析索引数据"""
    # json.loads()对JSON数据进行解码,转换成一个字典
    data = json.loads(html)
    # 当data这个字典存在且'data'键名存在于data字典中。data.keys()返回data这个字典所有的键名
    if data and 'data' in data.keys():
        # get() 函数返回字典中指定键的值，在这里遍历data字典中键名为'data'的
        # 值，每个元素分别为一个图集。
        for item in data.get('data'):
            # 对于'data'的值中的每个元素，建立一个生成器，得到每个网址
            yield item.get('article_url')  # 'article_url'中信息是每个图集的网址

def get_page_detail(url):
    """ 拿到详情页图的信息"""
    try:
        # 此处不加headers会导致访问详情页失败
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错', url)
        return None

def parse_page_detail(html, url):
    """ 解析详情页"""
    # 声明解析后的网页对象
    soup = BeautifulSoup(html, 'lxml')
    # 通过传入css选择器，选择第一个<title>标签，获取文本内容，就是图集的标题。
    title = soup.select('title')[0].get_text()
    # 声明一个正则表达式对象，来匹配我们想要的Json语句。注意re.S使 . 能匹配任意字符。
    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\),', re.S)
    result = re.search(images_pattern, html)
    # 注意：这里的Json语句包含转义字符 \ ，不去掉会报错
    result = result.group(1).replace('\\', '')
    # result = re.sub(r'\\', '', result.group(1))
    if result:  # 结果存在则进行
        data = json.loads(result)  # 把Json转换为字典
        if data and 'sub_images' in data.keys():
            # 'sub_images'这个键的值是一个列表，里面每个元素是字典，包含每个图集的地址。
            sub_images = data.get('sub_images')   # 得到图集的地址
            images = [item.get('url') for item in sub_images]  # 构造一个图集列表，包含每个图片的地址。
            for image in images:
                download_image(image)  # 下载每张图片
            return {  # 返回一个字典，格式化数据，准备存入MongoDB
                'title': title,
                'url': url,
                'images': images,
            }

def download_image(url):  # 传入的是每张图片的地址
    """ 下载图片"""
    print('正在下载', url)  # 调试信息
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                 '(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_image(response.content)  # 保存图片，content返回二进制内容（当保存图片视频时）
        return None
    except RequestException:
        print('请求图片出错', url)
        return None

def save_image(content):
    """存图片"""
    # 定义文件路径，文件名把图片信息md5加密，保证每个文件名不同。
    file_path = '{0}/{1}.{2}'.format(os.getcwd() + '\images', md5(content).hexdigest(), 'jpg')
    #file_path = 'F:\\test'format('\images', md5(content).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):  # 如果文件不存在
        with open(file_path, 'wb') as f:
            f.write(content)
'''
w     以写方式打开，不存在则创建
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )'''

#存储到数据库
'''
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
# 其中MONGO_DB，MONGO_URL为配置文件中的参数
def save_to_mongo(result):
    """存储文件到数据库"""
    if db[MONGO_DB].insert(result):
        print('存储成功', result)
        return True
    return False
'''

def main(offset):
    """ 主函数"""
    html = get_page_index(offset, KEYWORD)  # 获取索引页网页内容
    for url in parse_page_index(html):  # parse_page_index()返回一个生成器，生成每个图集的地址
        html = get_page_detail(url)  # 得到每个图集详情页的内容
        if html:  # 如果内容返回成功
            result = parse_page_detail(html, url) # 解析详情页，返回一个字典结果
            #save_to_mongo(result)  # 存入数据库

if __name__ == '__main__':
    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]  # 生成一个offset列表
    pool = Pool()  # 声明一个进程池
    pool.map(main, groups)
    pool.close()
    pool.join()