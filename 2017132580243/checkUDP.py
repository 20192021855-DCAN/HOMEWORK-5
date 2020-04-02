def checkUDP(data):

    sum = 0x0000

    for temp in data:
        sum = sum + (temp & 0xffff)

        # 溢出回卷
        if sum < 0xffff:
            sum = (sum >> 16) + (sum & 0xffff)

    #取反
    return ~sum


def checkUdpAns(ans, data):

    if ans + data[0] + data[1] + data[2] == -1:
        print('正确')
    else:
        print('失败')


# 测试数据
data = [0b0110011101100000, 0b0101011101010111, 0b1000111110001111]

# 校验和
ans = checkUDP(data)

# 检测UDP校验和是否正确
checkUdpAns(ans, data)
