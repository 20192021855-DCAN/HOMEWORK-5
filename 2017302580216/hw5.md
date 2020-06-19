## 一：UDP校验和

```python
def check(datas):
    _sum=0
    for _data in datas:
        _sum=_data+_sum
    _sum=displacement(_sum)
    _sum ^= 0xffff
    return _sum
def displacement(data):
    while True:
        _low = data & 0xffff
        _high = data >> 16
        if _high>0:
            data=_low+_high
        else:
            return data


datas = [0b0110011001100000, 0b0101010101010101, 0b1000111100001100]
if __name__ == '__main__':
    sum=check(datas) + datas[0] + datas[1] + datas[2]
    sum=displacement(sum)
    if  sum== 0xffff:
        print('正确')
    else:
        print('错误')


```



## 二：课后作业

#### p2：


A:
设主机A、B和C的IP地址分别为a、b、c。

主机A：源端口=80，源IP地址=b，DEST端口=26145，DESTIP地址=a

到主机C，左进程：源端口=80，源IP地址=b，DEST端口=7532，DESTIP 地址=c

到主机C，右进程：源端口=80，源IP地址=b，DEST端口=26145，DEST IP地址=c。

B)是的，Bob仍然需要执行并行下载；否则，他将获得比其他四个用户更少的带宽。

#### p4：

A：

​	**a**:01011100+ 01100101 = 11000001,所以反码是**00111110**

​	**b**:11011010+ 01100101 =100111111,所以反码是**011000000**

​	**c**:a 中的第一、二字节变为 01011101、01100100
