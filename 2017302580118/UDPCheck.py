from past.builtins import raw_input

# 从键盘读取第一个运算值
str1 = raw_input("请输入第一个值：")
# 从键盘读取第二个输入值
str2 = raw_input("请输入第二个值：")

# 计算二进制相加结果的函数
def addBineary(a,b):
    a = int(a,2)
    b = int(b,2)
    return bin(a+b)[2:]

# 中间结果
print("------------------")
print("中间结果")
temp = addBineary(str1,str2)
print(temp)

# 回卷
print("------------------")
print("回卷")
print("和")
# 取去掉最高位后的二进制值
addition = addBineary(temp[0],temp[1:])
print(addition)

# 校验和
print("------------------")
print("校验和")
result = addition.replace('1','2').replace('0','3')
result = result.replace('2','0').replace('3','1')
print(result)
