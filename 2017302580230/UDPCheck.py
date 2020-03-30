import numpy as np


# 格式无误返回0，否则返回-1
def isBinary(nums: list) -> int:
    if len(nums) <= 0:
        return -1
    for num in nums:
        if len(num) != 16:
            return -1
        for n in num:
            if n != '0' and n != '1':
                return -1
    return 0


# 返回数据总和
def getSum(nums: list) -> int:
    value = 0             # 校验和
    maximum = pow(2, 16)  # 用于取余
    for num in nums:
        value += int(num, 2)
        if value >= maximum :
            value = value % maximum  + value / maximum
    return int(value)


# 两者和不包含0返回0，否则返回-1
def check(nums: list, sum_value: int) -> int:
    if ~getSum(nums) != sum_value:
        return -1
    return 0


if __name__ == "__main__":
    nums = ['0110011001100000', '0101010101010101', '1000111100001100']
    print("输入数据为：")
    for num in nums:
        print(num)
    if isBinary(nums) == 0:
        sum_value = ~getSum(nums)
        print("校验和为：" + np.binary_repr(sum_value, width=16))
        result = check(nums, sum_value)
        if result != 0:
            print("分组出现差错.")
        else:
            print("接受方处和为: 1111111111111111.")
    else:
        print("Data error in form.")
