import requests

url = 'https://www.ccv.adobe.com/v1/player/ccv/9kohKER9FYz/embed?bgcolor=%23191919/'
response = requests.get(url)
html = response.text
print(html)