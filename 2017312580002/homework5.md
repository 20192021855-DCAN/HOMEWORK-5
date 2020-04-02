## Homework 5

2017312580002-周梓浩

------

計算UDP校檢和

```python
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
```

結果為:

```
1011010100111101
```

<img src="C:\Users\junow\Desktop\UDPCheckSum.png" alt="UDPCheckSum" style="zoom:72%;" />

------

### P3

01010011+01100110+01110100=100101101

回卷:00101101+1=00101110

取反:11010001

使用反碼的原因：不依赖于系统的大小端、計算方便。

如何檢測：接收方将三个原始數据与校驗和相加，和包含0則出錯。

1比特的差錯必定可以檢測出來,2比特可能檢測不出

#### P4

a. 01011100+01100101 = 11000001 反碼為00111110

b. 11011010+01100101 = 100111111 反碼為01100000

c. 两个字节的最低位都发生反转，变成01011101和01100100
01011101+01100100=11000001 反码为00111110 未发生改变
