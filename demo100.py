# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
# num = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i != j) and (j != k) and (k != i):
#                 print(i,j,k)
#                 num += 1
# print("满足条件的数字个数为：", num)

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
# 低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
# i= int(input("净利润："))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         print("提成：", (i - arr[idx]) * rat[idx])
#         i = arr[idx]
# print("总提成：", r)

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# list = []
# for i in range(3):
#     x = int(input('integer:\n'))
#     list.append(x)
# list.sort()
# print(list)

# Python 阿姆斯特朗数
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
# Python 检测用户输入的数字是否为阿姆斯特朗数

# 获取用户输入的数字
# num = int(input("请输入一个数字："))
# # 初始化变量 sum
# sum = 0
# # 指数
# n = len(str(num))
# # 检测
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10
# # 输出结果
# if num == sum:
#     print(num, "是阿姆斯特朗数")
# else:
#     print(num, "不是阿姆斯特朗数")

# import random
#
# print(random.randint(0,9))

# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}X{}={}\t'.format(j,i,i*j),end='')
#     print()

# Python 生成日历
# 引入日历模块
import calendar
# 输入指定年月
yy = int(input("输入年份："))
mm = int(input("输入月份："))
# 显示日历
print(calendar.month(yy,mm))