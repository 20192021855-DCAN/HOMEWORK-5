import numpy as np


def checksum(datas):
    result = 0
    for i in datas:
        result += i;
        if result > 0xffff:
            result = (result & 0xffff) + 1
    result = result ^ 0xffff
    return result


if __name__ == '__main__':
    datas = [int('0110011001100000',2),int('0101010101010101',2),int('1000111100001100',2)]
    res = checksum(datas)
    print("correct_result:1011010100111101")
    print("check_result:" + np.binary_repr(res))
    print("1011010100111101".__eq__(np.binary_repr(res)))