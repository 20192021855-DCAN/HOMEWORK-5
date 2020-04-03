import numpy as np

def checkSum(list):
    result = 0
    for bits in list:
        result += int(bits, 2);                     # 加总
    result = (result % (1 << 16)) + (result >> 16)  # 回卷
    return ((1 << 16) - 1) & ~result                # 取反

if __name__ == '__main__':
    datagram = ["0110011001100000", "0101010101010101", "1000111100001100"]
    myResult = checkSum(datagram)
    print("正确的检验和为: 1011010100111101")
    print("计算出的检验和: " + bin(myResult)[2:])

