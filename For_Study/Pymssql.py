import pymssql
import Order_E3_EZR

# 加载基础模块
# 基本参数定义
# 驿客接口文档http://doc.ezrpro.com/article/f7bda44f0873e7fcb23995a79d2fbda1
# 设置主程序
#     判断模块启用情况
#     调用各模块
# 获取Token方法
# 定义数据库查询方法


def BSERP_XZ_Data():
    server = '127.0.0.1'
    user = 'sa'
    password = 'x24681012'
    database = 'BSERP_XZ'
    port = '1433'
    tds_version = '4.2'  # 指定tds版本，防止版本过高，不能执行
    conn=pymssql.connect()
    # 连接数据库
    conn = pymssql.connect(
        server=server,
        user=user,
        password=password,
        database=database,
        port=port,
        charset='GBK',  # 有时候去掉charset和tds才行？
        tds_version=tds_version
    )
    if conn:
        return conn


#执行数据库查询
def select_ipos(sql):
    conn=BSERP_XZ_Data()
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()
    return cur


#执行数据库写入
def exec_ipos(sql):
    print('IPOS数据库写入')
    conn=BSERP_XZ_Data()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur


def main():
    print('根据时间执行计划任务')
    #Order_E3_EZR.ipos_des()
    Order_E3_EZR.ipor_mb()

if __name__ == '__main__':
    main()






"""
cur=conn.cursor()
#cur.execute('SELECT  getdate()')
cur.execute('SELECT top 5 KHDM,KHMC FROM KEHU')


#cur.execute('insert into [dbo].[BANZU](BZDM)values (111)')
#conn.commit()
#str=cur.fetchall()

row=cur.fetchone()
while row:
    print(row[0]+row[1])
    row=cur.fetchone()

print(cur.fetchall())
cur.close()
conn.close()
print('123')
"""


#import os
#import pymssql

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

