num = input("请输入16比特字数：")
UDP = []
checksum = 0


def Inverse(sum):
    listSum = list(sum)
    for i in range(len(sum)):
        if (listSum[i] == '0'):
            listSum[i] = '1'
        else:
            listSum[i] = '0'
    return ''.join(listSum)


for i in range(0, int(num)):
    udp_num = input("请输入第" + str(i + 1) + "个16比特字：")
    UDP.append(udp_num)
for i in range(0, int(num)):
    checksum += int(UDP[i], 2)
if len(str(bin(checksum))) > 18:
    checksum += 1
    print("校验和为：" + Inverse(str(bin(checksum))[3:]))
else:
    print("校验和为："+Inverse(str(bin(checksum))[2:]))