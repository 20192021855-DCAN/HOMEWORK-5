num1 = '0110011001100000'
num2 = '0101010101010101'
num3 = '1000111100001100'
num1 = int(num1,2)
num2 = int(num2,2)
num3 = int(num3,2)
#num1与num2求和  进位则回卷 而四字节二进制数位数为18位 进位大于18
if len(bin(num1+num2)) > 18:
    add_1 = int(str(bin(num1+num2))[3:],2 )+1
else:
    add_1 = int(str(bin(num1 + num2))[2:], 2)
#同理
if len(bin(num3+add_1)) > 18:
    add_2 = int(str(bin(num3 + add_1))[3:], 2) + 1
else:
    add_2 = int(str(bin(num1 + add_1))[2:], 2)
add_2 = str(bin(add_2)[2:])

while len(add_2)!=16:
    add_2 = "0"+add_2
result = ""
#取反
for i in add_2:
    if i == "0":
        result += "1"
    else:
        result += "0"
print("最终结果")
print(result)


