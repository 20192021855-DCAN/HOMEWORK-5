# -*- coding: utf-8 -*-
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def checksum(datagram):
    sum = 0x0
    for data in datagram:
        sum += data
        if sum > 0xffff:
            sum = sum & 0xffff
            # 溢出回卷至最低位
            sum += 1
    # 返回16位和反码
    return (~sum) & 0xffff


datagram =[int('0110011001100000',2),int('0101010101010101',2),int('1000111100001100',2)]
sum = checksum(datagram)
print("校验结果："+ str((sum == int('1011010100111101',2))))