import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import pandas
from bs4 import BeautifulSoup
import re
import lxml


def get_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3
    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(data)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(url)
            return response.text
        return None
    except RequestException:
        print('请求的索引出错')
        return None


def parse_page_index(html):
    data = pandas.json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求的详情页出错', url)
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('BASE_DATA.galleryInfo = (.*?);', re.S)
    result = re.search(images_pattern, html)
    print(html)
    print(result, 'OK')
    if result:
        data = pandas.json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            return {
            'title':title,
            'url': url,
            'images':images
        }


def main():
    html = get_page_index(0, '街拍')  #获取主查询页面
    for url in parse_page_index(html):#查询分页面
        url2 = url.replace('group/', 'a')
        html = get_page_detail(url2)
        if html:
            result = parse_page_detail(html, url2)
            print(result)


main()












#if __name__ == '___main__':
#    main()



