import pymssql
import Order_E3_EZR
import pymysql
import time

# 加载基础模块
# 基本参数定义
# 驿客接口文档http://doc.ezrpro.com/article/f7bda44f0873e7fcb23995a79d2fbda1
# 设置主程序
#     判断模块启用情况
#     调用各模块
# 获取Token方法
# 定义数据库查询方法


def Conn_Ipos():
    db=pymysql.connect('192.168.0.9','ipos','ipos!@#','ipos')
    if db:
        return db

#执行数据库查询
def select_ipos(sql):
    db=Conn_Ipos()
    cur=db.cursor()
    cur.execute(sql)
    db.close()
    return cur


#执行数据库写入
def exec_ipos(sql,param):
    print('IPOS数据库写入')
    db=Conn_Ipos()
    cur = db.cursor()
    cur.execute(sql,param)
    db.commit()
    db.close()
    return cur


def main():
    print('根据时间执行计划任务')
    #Order_E3_EZR.ipos_ETL()
    i=1
    while ( 1==1 ):
        print(i)
        i=i+1
        time.sleep(0.1)


if __name__ == '__main__':
    main()
