import pymssql
import xlwt
import calendar


# 数据库连接信息
server = '192.168.0.11'
user = 'sa'
password = 'bsxz@#$%'
database = 'BSERP_XZ'
port = '2433'
tds_version = '4.2'  # 指定tds版本，防止版本过高，不能执行
# charset='UTF-8'
# 连接数据库
conn = pymssql.connect(
    server=server,
    user=user,
    password=password,
    database=database,
    port=port,
   #  charset=charset,
    tds_version=tds_version
)

cursor = conn.cursor()
input("Press <enter>")