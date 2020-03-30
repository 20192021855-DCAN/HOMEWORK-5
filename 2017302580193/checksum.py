import numpy as np

def getChecksum(data_bits: list) -> int:
    res = 0
    for bit_word in data_bits:
        res += bit_word
        if res > 0xffff:
            res = (res % (1 << 16)) + (res >> 16)
    res = np.invert(res)
    return res

if __name__ == '__main__':
    data_bits = [int("0110011001100000", 2), int("0101010101010101", 2), int("1000111100001100", 2)]
    checksum = getChecksum(data_bits)
    print("3个16比特的字分别为：" + "0110011001100000 " + "0101010101010101 " + "1000111100001100")
    print("实际的校验和为：" + "1011010100111101")
    print("计算得到的校验和为：" + np.binary_repr(checksum, width = 16))
    print("1011010100111101" == np.binary_repr(checksum, width = 16))