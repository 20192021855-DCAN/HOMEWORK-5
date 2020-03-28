import matplotlib.pyplot as plt
import numpy as np
import sys

def calCheckSum(list):
    if len(list)<2:
        print("计算字节数量需要大于等于2")
        return 0
    sum=0
    for i in list:
        sum+=int(i,2)
    sum=bin(sum).replace('0b','')
    if len(sum) > 16:
        over=sum[0:len(sum)-16]
        conservation=sum[len(sum)-16:]
        bin_sum=bin(int(conservation,2)+int(over,2)).replace('0b','')
        # 上述转换会导致第一位为0时，0被省略，所以做判断<16，加上0
        if len(bin_sum) < 16:
            bin_sum="0"+bin_sum
        checksum=bin_sum.replace('1','2').replace('0','1').replace('2','0')
        return checksum
    else:
        checksum=sum.replace('1','2').replace('0','1').replace('2','0')
        return checksum

def draw(wordlist,checksum):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set(xlim=[0,16],ylim=[-0.2,1.2],title='CheckSum and base word',ylabel='数值',xlabel='位置')
    i=1
    for word in wordlist:
        ylist=list(word)
        ynumbers=list(map(int,ylist))
        x=np.arange(16)
        # ax.scatter(x, ynumbers, label='word' + str(i))
        ax.plot(x, ynumbers, label='word' + str(i))
        i+=1
    checksumlist=list(checksum)
    cnumbers=list(map(int ,checksumlist))
    # ax.scatter([int(x) for x in range(0, 16)], cnumbers, label='checksum')
    ax.plot([int(x) for x in range(0, 16)], cnumbers, label='checksum')
    ax.legend()
    plt.show()

if "__main__" == __name__:
    biteList=[]
    while(True):
        flag=input("输入字节字，:q退出,:r采用默认测试")
        if flag == ":q":
            break
        elif flag == ":r":
            biteList+=["0110011001100000","0101010101010101","1000111100001100"]
            break
        else:
            biteList.append(flag)
    checksum=calCheckSum(biteList)
    draw(biteList,checksum)
    print(checksum)