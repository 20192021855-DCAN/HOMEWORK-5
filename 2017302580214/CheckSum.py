import matplotlib.pyplot as plt
import numpy as np
import sys

def checkSum(datas):
    # 逐个计算
    result = 0x0000
    for data in datas:
        result = result + data
        result = (result & 0xFFFF) + (result >> 16)
    #取反 
    result = 0xFFFF - result
    return result

def getList(number):
    y_axis=[]
    for i in range(16):
       y_axis.append( number & 0x1 )
       number = number >> 1
    return y_axis


if __name__ == '__main__':
    answer = 0b1011010100111101
    datas = [0b0110011001100000,0b0101010101010101,0b1000111100001100]
    result = checkSum(datas)
    print("checkSum:" + bin(checkSum(datas)).replace('0b', ''))
    print("answer:" + bin(answer).replace('0b', ''))
    plt.plot(np.arange(16),getList(datas[0]),"g",label='data1')
    plt.plot(np.arange(16),getList(datas[1]),"y",label='data2')
    plt.plot(np.arange(16),getList(datas[2]),"b",label='data3')
    plt.plot(np.arange(16),getList(result),"r",label='checkSum')
    plt.legend()
    plt.show()