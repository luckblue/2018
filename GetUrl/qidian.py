import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json

url = 'https://www.qidian.com/rank/yuepiao?style=1'
# url = 'https://www.qidian.com/free/all'
# url = 'http://read.qidian.com/chapter/dVQvL2RfE4I1/hJBflakKUDMex0RJOkJclQ2.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.status_code)
# html = response.text
# print(html)
print(soup)




