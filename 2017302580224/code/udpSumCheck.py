import numpy as np


def add(data1, data2):
    sum = x+y
    if sum >= 65536:
        sum = sum % 65536+1
        print(str(bin(data1))+" + "+str(bin(data2))+" wrap arround.")
    return sum


def check(sum, sumCheck):
    sum = sum+sumCheck
    if sum == 65535:
        print("和为"+str(bin(sum))+", 没有错误")
    else:
        print("和为"+str(bin(sum))+", 发生错误")


x = input("请输入一系列16比特字（二进制形式），输入#结束。\n请输入第1个字：")
x = int(x, 2)
i = 2
y = input("请输入第"+str(i)+"个字：")
while y != '#':
    y = int(y, 2)
    x = add(x, y)
    i = i+1
    y = input("请输入第"+str(i)+"个字：")
# x为和
sum = 65535-x
# sum为和的反码
print("和："+str(bin(x))+", 反码: "+str(bin(sum)))
check(x, sum)
