#-*-coding:utf8-*-
import itchat


def send_move():
    #nickname = input('please input your firends\' nickname : ' )
    #   想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
    users = itchat.search_friends(name='抗压青年人')
    #users = itchat.search_friends(name='抗压青年人')   # 使用备注名来查找实际用户名
    #获取好友全部信息,返回一个列表,列表内是一个字典
    print(users)
    #获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    itchat.send("该起来动一下了！",toUserName = userName)
    print('succeed')

if __name__=='__main__':
    itchat.auto_login(hotReload=True)  # 首次扫描登录后后续自动登录
    #获取好友列表
    users = itchat.get_friends()
    for i in users:
        print(i['NickName'])
    print(len(users))


    ## #发消息到个人
    # #users = itchat.search_friends(name='保哥')
    # #发消息到群聊
    # users = itchat.search_chatrooms(name='信息部')
    # print(users)
    # userName = users[0]['UserName']
    # itchat.search_friends()
    #
    # users = itchat.search_chatrooms(name='信息部')
    #
    # for i in range(1,10):
    #     itchat.send("保哥666   "+str(i), toUserName=userName)
    #     print('succeed')
