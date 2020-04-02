import numpy as np

def checksum(data_list):
    answer = 0
    for x in data_list:
        # 依次相加
        answer += x
        # 有溢出就回卷
        if answer > 0xffff:
            answer = (answer & 0xffff) + 1
    # 对结果取反得到校验和
    answer = answer ^ 0xffff
    return answer

if __name__ == '__main__':
    data_list = [int('0110011001100000', 2), int('0101010101010101', 2), int('1000111100001100', 2)]
    res = checksum(data_list)
    print("real_answer:1011010100111101")
    print("check_answer:" + np.binary_repr(res))
    print("1011010100111101".__eq__(np.binary_repr(res)))