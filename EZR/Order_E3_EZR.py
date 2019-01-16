#加载主模块
import main
import pymysql

#api = 'api/pbase/prodcrmupload'
#获取数据源
#写入数据目标
#数据处理


#https://www.jianshu.com/p/fba075a4cfe9

#数据处理单向
def ipos_ETL():
    sql="select spdm as spdm,spmc as spmc from ipos_lsxhdmx LIMIT 5 "
    Ipos=main.IPOS()
    cur=Ipos.select_ipos1(sql)
    row = cur.fetchone()
    while row:
        print(row[0]+' '+row[1])
        sql="INSERT into aaaaa_test(spdm,spmc)VALUES(%s,%s)"
        param=(row[0], row[1])
        Ipos.exec_ipos(sql, param)
        row = cur.fetchone()
    print('这里写入日志')
    Ipos.db.close()


