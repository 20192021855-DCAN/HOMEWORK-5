import numpy as np
from matplotlib import pyplot as plt
#获取UDP校验和
def get_sum(bit_list):
    sum=0
    for bit in bit_list:
        #超出16位直接返回
        if len(bit)>16:
            return
        sum+=int(bit,2)
        #回卷
        sum=(sum&0xffff)+((sum>>16)&0x1)
    #取反
    sum=sum^0xffff
    return sum

#画图
def showplt(bit_list,sum):
    plt.title("UDP_SUM")
    plt.xlabel("bit")
    plt.ylabel("value")
    #画出需要校验的数字的plt图
    for index in range(len(bit_list)):
        x = []
        y = []
        for i in range(16):
            x.append(i+1)
            y.append(int(bit_list[index][i]))
        plt.plot(x, y,label="num{0}".format(index+1))
    #画出UDP校验和的plt图
    x = []
    y = []
    for i in range(16):
        x.append(i + 1)
        y.append(int(sum[i]))
    plt.plot(x, y, label="UDPSUM")
    plt.legend(loc='upper left')
    plt.show()


if __name__=='__main__':
    list=["0110011001100000",
          "0101010101010101",
          "1000111100001100"]
    for i in range(len(list)):
        print("第{0}个校验数字为：{1}".format(i+1,list[i]))
    print("校验和为：{0}".format(np.binary_repr(get_sum(list),16)))
    showplt(list,str(np.binary_repr(get_sum(list),16)))