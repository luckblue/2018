import pymssql
import xlwt
import calendar


# 定义导出对账单函数
def output_dzd(WhereKhs, TabName):
    num = 0  # 计数
    for WhereKh in WhereKhs:
        num += 1
        print('查询第%s个客户%s的对账单！请稍等...' % (num, WhereKh[0]))

        # 查询结果
        cursor.execute(
            "select  KEHU.KHDM,KEHU.KHMC,A.RQ,"
            "(CASE WHEN A.LXDM='0' THEN '货品' WHEN A.LXDM='1' THEN '道具及其他' END) AS DJXZ,"
            "A.LXMC,A.DJBH,1 AS TZDH,"
            "A.ZY,A.QCQK,A.XHSL,A.XHJE,A.THSL,A.THJE,A.SKJE,A.DJSK,A.QMQK "
            "from " + TabName + " AS A inner join KEHU on kehu.khdm=A.khdm and A.KHDM='" + WhereKh[0] + "'"
            " left join PFXHD on PFXHD.DJBH=A.DJBH "
            "left join PFTHD on PFTHD.DJBH=A.DJBH "
        )

        records = cursor.fetchall()

        # 创建工作表对象，并设置编码格式
        work_book = xlwt.Workbook(encoding='gbk')
        # 添加一个sheet表，参数为sheet的表名
        sheet = work_book.add_sheet('对账单')

        # 写入表头数据
        sheet.write(0, 0, '客户代码')
        sheet.write(0, 1, '客户名称')
        sheet.write(0, 2, '日期')
        sheet.write(0, 3, '单据类型')
        sheet.write(0, 4, '单据性质')
        sheet.write(0, 5, '单据编号')
        sheet.write(0, 6, '通知单号')
        sheet.write(0, 7, '摘要')
        sheet.write(0, 8, '期初欠款')
        sheet.write(0, 9, '发货数量')
        sheet.write(0, 10, '发货金额')
        sheet.write(0, 11, '退货数量')
        sheet.write(0, 12, '退货金额')
        sheet.write(0, 13, '收款金额')
        sheet.write(0, 14, '定金金额')
        sheet.write(0, 15, '期末金额')

        row = 1

        for item in records:
            # sheet.write()是写入内容的方法，参数一表示行数，参数二表示列数，参数三表示要写入的内容
            sheet.write(row, 0, item[0])
            sheet.write(row, 1, item[1])
            sheet.write(row, 2, item[2], datastyle)
            sheet.write(row, 3, item[3])
            sheet.write(row, 4, item[4])
            sheet.write(row, 5, item[5])
            sheet.write(row, 6, item[6])
            sheet.write(row, 7, item[7])
            sheet.write(row, 8, item[8])
            sheet.write(row, 9, item[9])
            sheet.write(row, 10, item[10])
            sheet.write(row, 11, item[11])
            sheet.write(row, 12, item[12])
            sheet.write(row, 13, item[13])
            sheet.write(row, 14, item[14])
            sheet.write(row, 15, item[15])
            # print('已写入第%s行数据！' % row)
            row += 1

        # 保存EXCEL表
        work_book.save('D:\\对账单\\' + WhereKh[0] + '.xls')
        print('查询完成！文件路径为：D:\\对账单\\' + WhereKh[0] + '.xls')
        print('---------------------------------------')

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

# 日期格式
datastyle = xlwt.XFStyle()
datastyle.num_format_str = 'yyyy-mm-dd'

# 调用存储过程需要的参数
Year = input('请输入年份：')
Month = input('请输入月份：')
monthRange = calendar.monthrange(int(Year), int(Month))
Rq_S = Year+'-'+Month+'-01'                    # 起始日期
Rq_E = Year+'-'+Month+'-'+str(monthRange[1])   # 截止日期
TabName_SHES = 'ReportDzd_SHES'     # 临时表名字
TabName_COOL = 'ReportDzd_COOL'     # 临时表名字

# 查询所有未停用的茜子客户代码
cursor.execute("select KHDM from kehu where QDDM='000' and XZDM='0' and TZSY=0 and KHMC like 'shes%' order by KHDM")
WhereKhs_SHES = cursor.fetchall()        # 客户代码列表


# 查询所有未停用的酷尔客户代码
cursor.execute("select KHDM from kehu where QDDM='000' and XZDM='0' and TZSY=0 and KHMC not like 'shes%' order by KHDM")
WhereKhs_COOL = cursor.fetchall()        # 客户代码列表


# ******茜子客户对账单初始化******
print()
print("------茜子客户对账单初始化------")
print()
# SQL查询语句
sql = "exec CUS_XZ_KHWLZA20181106_SHES @Rq_S='"+Rq_S+"',@Rq_E='"+Rq_E+"',@WhereKh='"+''+"',@tabname='"+TabName_SHES+"'"
# 执行查询
# cursor.execute(sql)


# ******酷尔客户对账单初始化******
print("------酷尔客户对账单初始化------")
print()
# SQL查询语句
sql = "exec CUS_XZ_KHWLZA20181106_COOL @Rq_S='"+Rq_S+"',@Rq_E='"+Rq_E+"',@WhereKh='"+''+"',@tabname='"+TabName_COOL+"'"
# 执行查询
# cursor.execute(sql)

# ******茜子客户对账单导出******
print('茜子客户列表：')
print(WhereKhs_SHES)
print()
print('茜子客户总数为：%s' % len(WhereKhs_SHES))
print()
print("------开始导出茜子客户对账单------")
output_dzd(WhereKhs_SHES, TabName_SHES)
print("------茜子客户对账单导出完成------")
print()

# ******酷尔客户对账单导出******
print('酷尔客户列表：')
print(WhereKhs_COOL)
print()
print('酷尔客户总数为：%s' % len(WhereKhs_COOL))
print()
print("------开始导出酷尔客户对账单------")
output_dzd(WhereKhs_COOL, TabName_COOL)
print("------酷尔客户对账单导出完成------")

conn.close()

print()
input("Press <enter>")