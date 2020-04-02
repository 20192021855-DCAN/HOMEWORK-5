import numpy as np

def UDPcheck(data_list):
    answer = 0
    for x in num_list:
        # 依次相加
        answer += x
        # 有溢出就回卷
        if answer > 0xffff:
            answer = (answer & 0xffff) + 1
    # 对结果取反得到校验和
    answer = answer ^ 0xffff
    return answer

if __name__ == '__main__':
    print("num1:0110011001100000")
    print("num2:0101010101010101")
    print("num3:1000111100001100")
    num_list = [int('0110011001100000', 2), int('0101010101010101', 2), int('1000111100001100', 2)]
    res = UDPcheck(num_list)
    print("check_answer:" + np.binary_repr(res))
    print("接收方和：1111111111111111")