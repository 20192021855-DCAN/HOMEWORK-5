import matplotlib.pyplot as plt
import numpy as np

DIGIT_LENGTH = 16


def checksum(data_list):
    """Compute the Checksum"""
    result = 0
    # Compute the sum
    for t in data_list:
        result += t
        t = bin(t)[2:]
        t = str.zfill(t, DIGIT_LENGTH)
        print(t)
        t = np.asarray(list(t))
        plt.plot(t)
    # if the length of the result is more than 16, then rollback
    if result >= pow(2, DIGIT_LENGTH):
        result = result - pow(2, DIGIT_LENGTH) + 1
    # abs is to remove the symbol, [2:] is to remove 0b which is binary format in python
    result = bin(result ^ 0xFFFF)[2:]
    result = str.zfill(result, DIGIT_LENGTH)
    print('校验和为：' + result)
    result = np.asarray(list(result))
    plt.plot(result)
    plt.show()
    return result


if __name__ == '__main__':
    checksum([int('1001001001001001', 2),
              int('0100100a100100100', 2),
              int('1101101101101101', 2)])

