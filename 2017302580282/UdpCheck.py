# coding=utf-8

import numpy as np
import math
import matplotlib.pyplot as pl


def check_sum(c_list):
    num = 0
    for l in c_list:
        num = l + num
        num = (num & 0xffff) + (num >> 16)
    num = 0xffff - num
    return num


# 将传入的16位二进制数转换为数组
def binary_list(binary):
    bin_list = np.zeros(16)
    start = 16 - len(binary)
    for i in range(start, 15):
        bin_list[i] = binary[i - start]
    return bin_list


if __name__ == '__main__':
    udp_list = [0b0110011001100000, 0b0101010101010101, 0b1000111100001100]
    print("计算校验和为" + bin(check_sum(udp_list)).replace('0b', ''))
    # 画图
    y_list1 = binary_list(bin(udp_list[0]).replace('0b', ''))
    y_list2 = binary_list(bin(udp_list[1]).replace('0b', ''))
    y_list3 = binary_list(bin(udp_list[2]).replace('0b', ''))
    y_checkSum = binary_list(bin(check_sum(udp_list)).replace('0b', ''))

    fig = pl.figure()
    x_list = np.arange(0, 16)
    pl.subplot(411)
    pl.title("binary1")
    pl.xlim(0, 15)
    new_ticks = np.linspace(0, 15, 16)
    pl.xticks(new_ticks)
    pl.ylim(0, 1.1)
    pl.plot(x_list, y_list1, color="yellow")

    pl.subplot(412)
    pl.title("binary2")
    pl.xlim(0, 15)
    new_ticks = np.linspace(0, 15, 16)
    pl.xticks(new_ticks)
    pl.ylim(0, 1.1)
    pl.plot(x_list, y_list2, color="yellow")

    pl.subplot(413)
    pl.title("binary3")
    pl.xlim(0, 15)
    new_ticks = np.linspace(0, 15, 16)
    pl.xticks(new_ticks)
    pl.ylim(0, 1.1)
    pl.plot(x_list, y_list3, color="yellow")

    pl.subplot(414)
    pl.title("Check Sum")
    pl.xlim(0, 15)
    new_ticks = np.linspace(0, 15, 16)
    pl.xticks(new_ticks)
    pl.ylim(0, 1.1)
    pl.plot(x_list, y_checkSum, color="green")

    pl.show()



