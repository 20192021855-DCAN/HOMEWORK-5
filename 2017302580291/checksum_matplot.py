from matplotlib import pyplot as plt
import numpy as np
import random


def get_checksum(vars):
    '''
    发送端求得校验和
    :param vars: 16位整数所组成的数组
    :return: 校验和
    '''
    sum = 0
    for var in vars:
        sum += var
        if sum >= 0x10000:
            sum = (sum + 1) & 0xffff
    return ((~sum) & 0xffff)


def get_corrupt(exs, checksum):
    '''
    接收端检验是否有损
    :param exs: 16位整数组成的数组
    :param checksum: 校验和
    :return: 其和是否为0xFFFF
    '''
    sum = 0;
    for var in exs:
        sum += var;
        if sum >= 0x10000:
            sum = (sum + 1) & 0xffff
    sum += checksum
    return sum


def print_whether_corrupt(answer):
    '''
    根据Boolean值决定输出内容
    :param answer:
    :return:
    '''
    if(answer):
        print("\tUncorrupt")
    else:
        print("\tCorrupt")


def print_checksum(checksum):
    '''
    打印校验和
    :param checksum: 校验和
    :return:
    '''
    str = bin(checksum)
    print("校验和\n\t" + str.lstrip("0b").zfill(16))


def randomcolor():
    '''
    获取随机颜色
    :return:
    '''
    color = '#'
    for i in range(6):
        color += hex(random.randint(0,15)).lstrip("0x").zfill(1)
    return color


def get_y(var):
    '''
    获取y轴坐标
    :param var: y值
    :return: 16位组成的数组
    '''
    y = []
    for i in range(0, 16, 1):
        y.append(((var << i) & 0xffff) >> 15)
    return y


def drawit(vars, hascheck=False, check=0, sum=0):
    # x坐标
    x = [i for i in range(16)]
    for i in range(len(vars)):
        y = get_y(vars[i])
        plt.plot(x, y, lw=1, c=randomcolor(), marker='s', label='ex'+i.__str__())
    if hascheck:
        y = get_y(check)
        plt.plot(x, y, lw=1, c="red", marker='s', label='checksum')
        y = get_y(sum)
        plt.plot(x, y, lw=1, c="black", marker='s', label='sum')
    plt.xticks(x)  # x轴的刻度
    plt.xlim(-0.5, 15.5)  # x轴坐标范围
    plt.ylim(-0.1, 1.1)  # y轴坐标范围
    plt.title('Binary')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # 3.3.2 数据
    ex1 = 0b0110011001100000
    ex2 = 0b0101010101010101
    ex3 = 0b1000111100001100
    exs = [ex1, ex2, ex3]

    # 校验和
    checksum = get_checksum(exs)

    # 以二进制格式输出
    print_checksum(checksum)

    # 假设发送无损
    print("假设无损：")
    finalsum = get_corrupt(exs, checksum)
    print_whether_corrupt(finalsum == 0xffff)
    drawit(exs, True, checksum, finalsum)

    # 假设发送有损，ex1有误
    print("假设第一个数据有损：")
    exs[0] += 1
    finalsum = get_corrupt(exs, checksum)
    print_whether_corrupt(finalsum == 0xffff)
    drawit(exs, True, checksum, finalsum)