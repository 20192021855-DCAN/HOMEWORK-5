#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020-04-02 23:38:30
# @Author   : 张佳乐
# @Remarks  : python实现UDP的16位校检和
# @File     : UDP_check.py
# @Software : PyCharm
# Copyright © 2019 张佳乐. All rights reserved.

import numpy
from matplotlib import pyplot


def checksum_udp(udp_list):
    """
    UDP的16位校检和
    :param udp_list: 待校检16字数组
    :return: 校检和
    """
    check_sum = 0b0                                     # 二进制的0
    for i in udp_list:                                  # 将udp_list中的16字数依次相加
        i_to_binary = int(i, 2)
        check_sum += i_to_binary
        if check_sum > 0xffff:                          # 溢出的话回卷
            check_sum = (check_sum & 0xffff) + 1
    check_sum = numpy.binary_repr(check_sum ^ 0xffff)   # 取反
    return check_sum


# 实现书上3.3.2的例子
data = [
    '1101010101010101',
    '1110011001100110',
    '1000111100001100'
]
checksum = checksum_udp(data)
print('校验和为：' + checksum)

# 开始用matplotlib画图
x = range(1, 17)
for i in data:                                          # 分别绘制data中的数组
    pyplot.plot(x, list(i), label=i)
pyplot.plot(x, list(checksum))                          # 绘制结果
pyplot.legend(loc="lower right")                        # 展示标签
pyplot.show()                                           # 展示图片
