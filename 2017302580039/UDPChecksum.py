import numpy as np
from matplotlib import pyplot as plt


# 计算UDP校验和
def get_checksum(bit_list):
    checksum = 0
    for bit in bit_list:
        # UDP使用16比特的字来计算校验和
        if len(bit) != 16:
            print("输入数据出错，不是每个字的长度都为16比特！")
            return
        # 将二进制16比特字的字符串转化为int再求和
        checksum += int(bit, 2)
        # 回卷运算
        checksum = (checksum & 0xffff)+((checksum >> 16) & 0x1)
    # 取反
    checksum = checksum ^ 0xffff
    return checksum


# 绘制图表
def plot(bit_list, checksum):
    plt.xlabel("bit_position")
    plt.ylabel("value")
    for i in range(len(bit_list)):
        x = []
        y = []
        for j in range(16):
            x.append(j)
            y.append(int(bit_list[i][j]))
        plt.plot(x, y,label="bit_number" + str(i + 1))
    x = []
    y = []
    for i in range(16):
        x.append(i + 1)
        y.append(int(checksum[i]))
    plt.plot(x, y, label="checksum")
    plt.legend(loc='right')
    plt.show()


if __name__ == '__main__':
    test_list = ["0110011001100000", "0101010101010101", "1000111100001100"]
    origin_checksum = "1011010100111101"
    computed_checksum = np.binary_repr(get_checksum(test_list), 16)
    for index in range(len(test_list)):
        print("第 {0} 个 16 比特字为：{1}".format(index + 1, test_list[index]))
    print("课本3.3.2的UDP校验和为："+ origin_checksum)
    print("计算得到的UDP校验和为："+ computed_checksum)
    print("两个校验和相等为：{0}".format(origin_checksum == computed_checksum))
    plot(test_list, str(computed_checksum))
