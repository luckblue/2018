#加载主模块
import main

api = 'api/pbase/prodcrmupload'

#获取数据源

#写入数据目标

#数据处理

def ipos_des():
    cur = main.select_ipos('SELECT top 5 KHDM,KHMC FROM KEHU')
    row = cur.fetchone()
    while row:
        print(row[0] +' '+ row[1])
        row = cur.fetchone()
    cur.close()


def ipor_mb():
    cur=main.exec_ipos("insert into [dbo].[BANZU]([BZDM])values('123')")
    cur.close()


def ipos_ETL():
    print('处理')