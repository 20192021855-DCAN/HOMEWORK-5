import struct


def checksum(alist: list) -> int:
    res = 0
    for x in alist:
        res += x
        # 若加法有溢出，则回卷
        if res > 0xffff:
            res = (res & 0xffff) + 1
    res = res ^ 0xffff
    return res


if __name__ == '__main__':
    alist = [int('0110011001100000', 2), int('0101010101010101', 2), int('1000111100001100', 2)]
    res = checksum(alist)
    print("正确校验和为1011010100111101")
    print("函数得到的校验和为：" + bin(res))

