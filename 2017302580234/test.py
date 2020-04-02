add1 = input("校验和的第一个数")
add2 = input("校验和的第二个数")
length = len(add1) if add1 > add2 else len(add2)

max = 1
for i in range(length):
     max *=10

def change(str):
     listStr = list(str)
     for i in range(len(str)):
          if(listStr[i] == '0'):
               listStr[i] = '1'
          else:
               listStr[i] = '0'
     return ''.join(listStr)

result = int(add1,2) + int(add2,2)
binResult = bin(result)[2:]
if(len(str(binResult)) <= length):
     print("校验和计算：",binResult)
     print("反码结果：",change(binResult))
else:
     agResult = str(int(binResult,10) - max)
     finalResult = int(agResult,2) + 0b1
     print("校验和计算：", bin(finalResult)[2:])
     print("反码结果：",change(bin(finalResult)[2:]))







