def get_checksum(vars):
    '''
    发送端求得校验和
    :param vars: 16位整数所组成的数组
    :return: 校验和
    '''
    sum = 0
    for var in vars:
        sum += var
        if sum >= 0x10000:
            sum = (sum + 1) & 0xffff
    return ((~sum) & 0xffff)


def whether_corrupt(exs, checksum):
    '''
    接收端检验是否有损
    :param exs: 16位整数组成的数组
    :param checksum: 校验和
    :return: 其和是否为0xFFFF
    '''
    sum = 0
    for var in exs:
        sum += var
        if sum >= 0x10000:
            sum = (sum + 1) & 0xffff
    sum += checksum
    return sum == 0xffff


def print_checksum(checksum):
    '''
    打印校验和
    :param checksum: 校验和
    :return:
    '''
    str = bin(checksum)
    print("校验和\n\t" + str.lstrip("0b").zfill(16))


def print_result(answer):
    '''
    根据Boolean值决定输出内容
    :param answer:
    :return:
    '''
    if(answer):
        print("\tUncorrupt")
    else:
        print("\tCorrupt")


if __name__ == '__main__':
    # 3.3.2 数据
    ex1 = 0b0110011001100000
    ex2 = 0b0101010101010101
    ex3 = 0b1000111100001100
    exs = [ex1, ex2, ex3]

    # 校验和
    checksum = get_checksum(exs)

    # 以二进制格式输出
    print_checksum(checksum)

    # 检测是否损坏
    # 假设发送无损
    print("假设无损：")
    print_result(whether_corrupt(exs, checksum))

    # 假设发送有损，ex1有误
    print("假设第一个数据有损：")
    exs[0] += 1
    print_result(whether_corrupt(exs, checksum))
