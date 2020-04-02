import struct


def getCheckSum(nums: list) -> int:
    res = 0
    max = pow(2, 16)
    for num in nums:
        res += int(num, 2)
        # 若加法有溢出，则回卷
        if res > 0xffff:
            res = (res & 0xffff) + 1
    res = res ^ 0xffff
    return res


if __name__ == '__main__':
    nums = ['0110011001100000', '0101010101010101', '1000111100001100']
    res = getCheckSum(nums)
    print("正确校验和为1011010100111101")
    print("getCheckSum函数得到的校验和为：" + bin(res))