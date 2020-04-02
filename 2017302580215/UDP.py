import numpy as np

def udp_check_sum(data_list):
    ans = 0
    for i in data_list:
        ans += i
        if ans > 0xffff:
            ans = (ans & 0xffff) + 1
    ans = ans ^ 0xffff
    return ans


if __name__ == '__main__':
    data_list = [int('1101010101010101', 2), int('1110011001100110', 2), int('1000111100001100', 2)]
    result = udp_check_sum(data_list)
    print('校验和为：' + np.binary_repr(result))
© 2020 GitHub, Inc.
