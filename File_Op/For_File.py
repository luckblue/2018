import os
import sys

# f = open("forwrite.txt", "w+",encoding='utf-8')
# f.write("可以 ，你做的很好！ 6666")  # 此时文件对象在最后一行，如果读取，将读不到数据
# s=f.tell()     # 返回文件对象当前位置
# f.seek(0,0)    # 移动文件对象至第一个字符
# str=f.read()
# print(s,str,len(str))


# with open("foo.txt", "wb") as f:
#     f.write("123")


str = open("foo.txt",  "w+")
str.write('1233')
# print(str.re)