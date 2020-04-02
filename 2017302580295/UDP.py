def checkSum(ulist):
    sum = 0
    for c in ulist:
        sum += c
        #回卷
        sum = (sum & 0xffff) + (sum >> 16)
        result = sum ^ (0xffff)
    return result

if __name__ == '__main__':
    udp_list = [0b0110011001100000,
          0b0101010101010101,
          0b1000111100001100]
    testSum = 0b1011010100111101
    predSum = checkSum(udp_list)
    for i in range(0,len(udp_list)):
        print(str(i+1) + "：" + '{:016b}'.format(udp_list[i], 'b'))
    print("预测检验和：" + format(predSum, 'b'))
    print("待测检验和：" + format(testSum, 'b'))
    if bin(testSum) == bin(predSum):
        print("相等，正确。")
    else:
        print("不等，出现错误！")
