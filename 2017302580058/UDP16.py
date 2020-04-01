import matplotlib.pyplot as plt
import numpy as np
import sys

def checkSum(mylist):
    sum=0;
    index=pow(2,16)
    for num in mylist:
        sum+=int(num,2)
        sum=sum//index+sum%index
    return np.binary_repr(~sum,width=16)

def draw(lists,checksum):
    plt.rcParams['font.family'] = ['STFangsong']
    plt.title("按位画图")
    plt.xlabel("位")
    plt.ylabel("值")
    i = 1
    for word in lists:
        mmylist = list(word)
        ynumbers = list(map(int, mmylist))
        x = np.arange(16)
        plt.plot(x, ynumbers, label='第' + str(i)+'个字')
        i += 1
    mmmylist = list(checksum)
    mynumbers = list(map(int, mmmylist))
    x = np.arange(16)
    plt.plot(x, mynumbers, label='检验和')
    plt.legend(loc="lower right")
    plt.show()

if __name__ == '__main__':
    mylist=["0110011001100000","0101010101010101","1000111100001100"]
    checksum=checkSum(mylist)
    print("校验和："+checksum)
    draw(mylist,checksum)






