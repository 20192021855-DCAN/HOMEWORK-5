import matplotlib
from matplotlib import pyplot as plt
def Add(n1,n2):
    res = n1+n2
    res = (res&0xFFFF) + (res>>16)
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
    res=Add(Add(data[0],data[1]),data[2])
    res=~res&0xffff
    print("待验证的校验和\t",format(checksum, 'b'))
    print("计算的校验和\t",format(res,'b'))
    if checksum!=res:
        print("错误，二者不同")
    else:
        print("正确，二者相同")
    fig=plt.figure()
    ax1=fig.add_subplot(9,3,1)
    ax2=fig.add_subplot(9,3,2)
    ax3=fig.add_subplot(9,3,3)
    ax4=fig.add_subplot(9,3,7)
    ax5=fig.add_subplot(9,3,8)
    x,y=plotData(data[0])
    ax1.plot(x,y)
    ax1.set_xlabel("data[0]")
    x,y=plotData(data[1])
    ax2.plot(x,y)
    ax2.set_xlabel("data[1]")
    x,y=plotData(data[2])
    ax3.plot(x,y)
    ax3.set_xlabel("data[2]")
    x,y=plotData(res)
    ax4.plot(x,y)
    ax4.set_xlabel("计算校验和\n"+format(res, 'b'),fontproperties='SimHei',fontsize=10)
    x,y=plotData(checksum)
    ax5.plot(x,y)
    ax5.set_xlabel("待检校验和\n"+format(checksum, 'b'),fontproperties='SimHei',fontsize=10)
    plt.show()
