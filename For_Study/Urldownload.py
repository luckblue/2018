import requests
requests.__version__
#print("测试2")
text=requests.get("http://httpbin.org/get")
#text2=requests.get("https://video.pearvideo.com/mp4/adshort/20181208/cont-1488599-13338916_adpkg-ad_hd.mp4")
#print(text2.content)
print(text.text)
print(text.json())
print(type(text.json()))

response = requests.get('https://www.baidu.com/img/bd_logo1.png?where=super')
b = response.content
with open('D://fengjing.jpg','wb') as f:
    f.write(b)