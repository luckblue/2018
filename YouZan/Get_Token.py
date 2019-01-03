import requests
import json

#常量
Youzan_url = 'https://open.youzan.com/oauth/token' #有赞调用地址
client_id = '9a8e4eadb6ae221c09' #有赞云颁发给开发者的应用ID
client_secret = '1b764868f05ffdf4d7bf393bb5a631f9' #有赞云颁发给开发者的应用secret
grant_type = 'silent'  #授与方式（固定为 “silent”）
kdt_id = '42312280'  #授权给该应用的店铺id，控制台里可查看


APPID = 'wx5fd097be09b290b8' #公众号APPID
AppSecret = '9e9d45176e225bab201e8aac93fa821f'  #公众号AppSecret
Weixin_Url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' #公众号调用地址

    #获取有赞access_token
def get_youzan_access_token():
    if 1==1:
        youzan_data = {"client_id":client_id,"client_secret":client_secret,"grant_type":grant_type,"kdt_id":kdt_id}
        html_json=json.loads(requests.post(url=Youzan_url,data=youzan_data).text)
        time = html_json['expires_in']
        return html_json['access_token']
    else:
        return '获取的access_token'

#有赞通过手机号获取用户open_id
def get_youzan_OpenID(mobile):
    url = "https://open.youzan.com/api/oauthentry/youzan.user.weixin.openid/3.0.0/get"
    access_token = get_youzan_access_token()
    data = json.dumps({"country_code":"+86","mobile":mobile})
    url = "https://open.youzan.com/api/oauthentry/youzan.user.weixin.openid/3.0.0/get" + '?access_token=' + access_token + "&mobile="+mobile
    open_id = json.loads(requests.get(url).text)["response"]["open_id"]
    return open_id


    #公众号获取access_token,注意发送服务器IP地址必须在公众号的白名单中，否则无法获取。
def get_weixin_access_token():
    res=requests.get(Weixin_Url+APPID+'&secret='+AppSecret)
    weixin_access_token = json.loads(res.text)['access_token']
    return  weixin_access_token


def send_weixin_mes(mobile):
    #案例https://blog.csdn.net/weixin_41004350/article/details/78705415
    mobanid = '3pafHfNdhgDaUDGDb4vIIjK8oVr4olQn06fsN9DzqFM'  #消息模板ID，从公众号后台获取
    OPENID = get_youzan_OpenID(mobile) #从有赞通过手机查询获取
    access_token = get_weixin_access_token()
    data = {"touser":OPENID,"template_id":mobanid,"url":"http://www.shes.cn","topcolor":"#FF0000","data":{"first":{"value":"恭喜你购买成功！","color":"#173177"},"keyword1":{"value":"巧克力","color":"#173177"},"keyword2":{"value":"39.8元","color":"#173177"},"keyword3":{"value":"2014年9月22日","color":"#173177"},"keyword4":{"value":"39.8","color":"#173177"},"keyword5":{"value":"0","color":"#173177"},"remark":{"value":"欢迎再次购买！","color":"#173177"}}}
    response = requests.post(url='https://api.weixin.qq.com/cgi-bin/message/template/send?access_token='+access_token,data=json.dumps(data))
    print(response.text)

if __name__=='__main__':
     send_weixin_mes("13410376830")
     #get_weixin_access_token()

