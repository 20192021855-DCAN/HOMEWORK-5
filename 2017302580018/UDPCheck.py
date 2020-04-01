import numpy as np


def CheckSum(bits_list):
    sum = 0
    for bits in bits_list:
        sum += int(bits,2)
        if sum > 0xffff:
            sum = (sum & 0xffff) + (sum >> 16)
    sum = 0xffff - sum
    return sum

if __name__ == '__main__':
    bits_list = ["0110011001100000","0101010101010101","1000111100001100"]
    result = CheckSum(bits_list)
    print("得到校验和为"+np.binary_repr(result,width=16))