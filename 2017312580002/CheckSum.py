import matplotlib.pyplot as plt
import numpy as np
import sys

def calCheckSum(list):
    sum=0
    for i in range(0,len(list)):
        sum+=int(list[i],2)^0xffff
    sum=bin(sum).replace('0b','')
    while(len(sum)>16):
        sum=sum[1:len(sum)]
        sum=bin(int(sum,2)+1).replace('0b','')
        if len(sum) < 16:
            sum="0" + sum
    print(sum)
    return sum

def draw(bitList,checkSum):
    plt.title("checkSum")
    plt.xlabel("bit")
    plt.ylabel("value")
    for bits in bitList:
        x=[]
        y=[]
        for i in range(16):
            x.append(i + 1)
            y.append(int(bits[i]))
        plt.plot(x, y, label="word{0}".format(bitList.index(bits)+1))
        # 画出UDP校验和的plt图
    x=[]
    y=[]
    for i in range(16):
        x.append(i + 1)
        y.append(int(checkSum[i]))
    plt.plot(x, y, label="checkSum")
    plt.legend(loc='upper left')
    plt.show()

if "__main__" == __name__:
    list=["0110011001100000", "0101010101010101", "1000111100001100"]
    checkSum=calCheckSum(list)
    draw(list,checkSum)