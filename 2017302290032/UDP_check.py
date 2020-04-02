num_list = []
print('请输入一系列的16位整数，输入#则结束')
num = input()
while num != '#':
    num_list.append(int('0b' + num, 2))
    num = input()
check_sum = int('0b' + input('请输入检验和：\n'), 2)

sum = 0
for n in num_list:
    sum += n
    sum = (sum & 0xffff) + (sum >> 16)
print('所有整数和为：')
print(bin(sum).replace('0b','').rjust(16,'0'))
if (sum + check_sum) ^ 0xffff == 0:
    print('传输后报文没有检测到错误')
else:
    print('传输后报文检测到错误')
