#加载主模块
import main
import pymysql

#api = 'api/pbase/prodcrmupload'
#获取数据源
#写入数据目标
#数据处理

def ipos_des():
    sql="select spdm as spdm,spmc as spmc from ipos_lsxhdmx LIMIT 5 "
    cur = main.select_ipos(sql)
    return cur


def ipor_mb():
    cur=main.exec_ipos("insert into [dbo].[BANZU]([BZDM])values('123')")
    cur.close()


def ipos_ETL():
    print('处理')
    cur=ipos_des()
    row = cur.fetchone()
    while row:
        print(row[0]+row[1])
        sql="INSERT into aaaaa_test(spdm,spmc)VALUES(%s,%s)"
        param=(row[0], row[1])
        main.exec_ipos(sql, param)
        row = cur.fetchone()
    cur.close()