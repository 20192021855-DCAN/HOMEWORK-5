import matplotlib
from matplotlib import pyplot as plt
def checkSum(data):
    res = data[0] + data[1]
    res = (res&0xFFFF) + (res>>16)
    res = res + data[2]
    res = (res & 0xFFFF) + (res >> 16)
    return res

def plotData(num):
    bin_num = bin(num)[2:].zfill(16)
    length = len(bin_num)
    x = []
    y = []
    for i in range(length):
        x.append(i)
        y.append(bin_num[i])
    return x,y


if __name__ == '__main__':
    checksum = 0b1011010100111101
    data = [0b0110011001100000,0b0101010101010101,0b1000111100001100]
    res = checkSum(data)
    print("和："+bin(res)[2:].zfill(16))
    print("校验和：" + bin(checksum)[2:].zfill(16))
    x,y = plotData(res)
    plt.plot(x,y,"b")
    x, y = plotData(checksum)
    plt.plot(x, y, "r")
    plt.show()