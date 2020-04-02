
# 计算UDP校验和
def calculateUDP(data):
    sum = 0x0
    for d in data:
        sum = sum + (d & 0xffff)
        if sum < 0xffff:
            sum = (sum >> 16) + (sum & 0xffff)
    # 取反
    return ~sum

#验证UDP校验和
def checkUDP(ans, data):
    if ans + data[0] + data[1] + data[2] == -1:
        print('校验结果正确')
    else:
        print('校验结果失败')

if __name__ == '__main__':
    data = [0b0110011001100000, 0b0101010101010101, 0b1000111100001100]
    result = calculateUDP(data)
    checkUDP(result, data)
