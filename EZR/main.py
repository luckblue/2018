
# 加载基础模块
# 基本参数定义
# 驿客接口文档http://doc.ezrpro.com/article/f7bda44f0873e7fcb23995a79d2fbda1
# 设置主程序
#     判断模块启用情况
#     调用各模块
# 获取Token方法
# 定义数据库查询方法


import pymssql
server = '127.0.0.1'
user = 'sa'
password = 'x24681012'
database = 'BSERP_XZ'
port = '1433'
tds_version = '4.2'  # 指定tds版本，防止版本过高，不能执行

# 连接数据库
conn = pymssql.connect(
    server=server,
    user=user,
    password=password,
    database=database,
    port=port#,
    #charset='utf8',
    #tds_version=tds_version
)

cur=conn.cursor()
cur.execute('SELECT  TOP 10 KHDM,KHMC from KEHU ')
#str=cur.fetchall()

row=cur.fetchone()
while row:
    print(row[0]+' '+row[1])
    row=cur.fetchone()

#print(cur.fetchall())
cur.close()
conn.close()
print('123')































import os
import pymssql

# server = "localhost:1433"
# user = "sa"
# password = "x24681012"
# conn = pymssql.connect(server,user,password,database="BSERP_XZ")
# # cursor=conn.cursor()
# # cursor.execute("""select getdate()""")
# # row=cursor.fetchone()
# # while row:
# #     print("sqlserver version:%s"%(row[0]))
# #     row=cursor.fetchone()
#
# conn.close()


#  数据库连接信息
# server = '192.168.0.13'
# user = 'report'
# password = 'report2015'
# database = 'ShesBI'
# port = '2433'
# print("1111")
# # 连接数据库
# conn = pymssql.connect(host='192.168.0.13', user='report', password='report2015', database='ShesBI', charset='utf8', tds_version='8.0')
# conn.cursor()
# print("1")
# cursor = conn.cursor()
# sql="select getdate()"
# cursor.execute(sql)
# print("12")
# row=cursor.fetchone()
# while row:
#     print("sqlserver version:%s"%(row[0]))
#     row=cursor.fetchone()
# print("123")
# conn.close()