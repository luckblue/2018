import requests
from lxml import etree

class Spider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "https://www.mzitu.com/"
        }

    def start_request(self):
        for i in range(1, 205):
            print("==========正在抓取%s页图片==========" % i)
            # 1. 获取整体数据  requests
            if i == 1:
                response = requests.get("https://www.mzitu.com")
            else:
                response = requests.get("https://www.mzitu.com" + "/page/" + str(i))
            html = etree.HTML(response.content.decode())
            self.xpath_data(html)

    def xpath_data(self, html):
        # 2. 获取想要的数据  lxml xpath
        src_list = html.xpath('//img[@data-original]/@data-original')
        alt_list = html.xpath('//img[@data-original]/@alt')
        for src, alt in zip(src_list, alt_list):
            response = requests.get(src, headers=self.headers)
            file_name = alt + ".jpg"
            print("正在抓取图片：" + file_name)
            # 3. 数据存储  with open
            with open(file_name, "wb") as f:
                f.write(response.content)


spider = Spider()
spider.start_request()