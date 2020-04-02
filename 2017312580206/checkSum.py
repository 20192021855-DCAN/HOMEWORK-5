
# coding: utf-8


import numpy as np


def getSum(nums:list)->int:
    tmp = nums[0] + nums[1]
    tmp = (tmp&0xFFFF) + (tmp>>16)
    tmp = tmp + nums[2]
    tmp = (tmp&0xFFFF) + (tmp>>16)
    return tmp


if __name__ == '__main__':
    nums = [0b0110011001100000, 0b0101010101010101, 0b1000111100001100]
    tmpSum = getSum(nums)
    checkSum = ~tmpSum
    #np.binary_repr()函数规定以二进制展示，并限定长度
    print("和： "+ np.binary_repr(tmpSum,width=16))
    print("校验和：" + np.binary_repr(checkSum,width=16))
    print("接收方处和：" + np.binary_repr(tmpSum+checkSum,width=16))





