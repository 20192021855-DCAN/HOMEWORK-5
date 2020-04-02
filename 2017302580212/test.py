import numpy as np
def checkSum(data):
    sum = 0
    for i in data:
        sum += i
        if sum > 0xffff:
            sum = (sum & 0xffff) + 1
    sum = np.invert(sum)
    return sum

if __name__ == '__main__':
    data = [int("0110011001100000", 2), int("0101010101010101", 2), int("1000111100001100", 2)]
    checksum = checkSum(data)
    print("校验和为："+"1011010100111101")
    print("计算后的校验和："+np.binary_repr(checksum))
    print("1011010100111101".__eq__(np.binary_repr(checksum)))