import matplotlib
from matplotlib import pyplot as plt
def check(data):
    ans = 0
    for c in data:
        ans += c
    ans = (ans & 0xffff) + (ans >> 16)
    return 0xffff - ans

def show(num):
    x = []
    y = []
    bin_num = bin(num)[2:].zfill(16)
    for i in range(len(bin_num)):
        x.append(i)
        y.append(bin_num[i])
    return x,y

def init():
    data = [0b0110111001100001,
            0b0110111000101111,
            0b1100111100001100,
            0b1111111100001100]
    #假设校验和位于第三个16位序列
    checkCode = data[2]
    ans = check(data)
    print("预期和：" + bin(ans)[2:].zfill(16))
    print("校验和：" + bin(checkCode)[2:].zfill(16))
    if(ans==checkCode):
        print("检验成功")
    else:
        print("检验失败")
    x, y = show(ans)
    plt.plot(x, y, "bo")
    x, y = show(checkCode)
    plt.plot(x, y, "ro")
    plt.show()

init()
