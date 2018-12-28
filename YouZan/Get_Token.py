import requests
import json

#有赞获取信息
# url='https://open.youzan.com/oauth/token'
# client_id = '9a8e4eadb6ae221c09'
# client_secret = '1b764868f05ffdf4d7bf393bb5a631f9'
# grant_type = 'silent'
# kdt_id = '42312280'
# url2=url+'?client_id='+client_id+'&client_secret='+client_secret+'&grant_type='+grant_type +'&kdt_id='+kdt_id
# html = requests.get(url2)
# print(json.loads(html.text)['access_token'])

#公众号获取信息
APPID = 'wx5fd097be09b290b8'
AppSecret = '9e9d45176e225bab201e8aac93fa821f'
access_token=requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+APPID+'&secret='+AppSecret)
print(json.loads(access_token.text))
print(json.loads(access_token.text)['access_token'])


#案例https://blog.csdn.net/weixin_41004350/article/details/78705415
mobanid='WEn581UTbPn7sXP-fQFEOokbkNRL1Iy6kYwdihGUoYE'
data = {"touser":"OPENID","template_id":"3pafHfNdhgDaUDGDb4vIIjK8oVr4olQn06fsN9DzqFM","url":"http://weixin.qq.com/download","topcolor":"#FF0000","data":{"User":{"value":"黄先生","color":"#173177"},"Date":{"value":"06月07日 19时24分","color":"#173177"},"CardNumber":{"value":"0426","color":"#173177"},"Type":{"value":"消费","color":"#173177"},"Money":{"value":"人民币260.00元","color":"#173177"},"DeadTime":{"value":"06月07日19时24分","color":"#173177"},"Left":{"value":"6504.09","color":"#173177"}}}

response = requests.post(url='http://www.baidu.com',data=json.dumps(data))
