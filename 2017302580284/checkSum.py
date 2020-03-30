from math import pi, sin

import numpy as np
from matplotlib import pyplot as plt

input_list = [0b0110011001100000, 0b0101010101010101, 0b1000111100001100]
expectAns = 0b1011010100111101


def check_sum(i_list):
    ans = 0
    for d in i_list:
        ans += d
    ans = (ans & 0xffff) + (ans >> 16)
    return 0xffff - ans


ans = check_sum(input_list)
print("expectAns=" + bin(expectAns))
print("ans=" + bin(ans))
is_correct = ans == expectAns
print("验证结果为：", is_correct)


# bin()类型转01数组
def bin_to_list(bin_str):
    arr = np.zeros(16, dtype=np.int)
    i = 18 - len(bin_str)
    for index in range(0, i):
        arr[index] = 0
    for index in range(2, len(bin_str)):
        arr[i + index - 2] = bin_str[index]
    return arr


fig = plt.figure(figsize=(12,9))
x_arr = np.arange(0, 16)
y_arr = bin_to_list(bin(input_list[0]))
plt.subplot(231)
plt.title("param1")
plt.plot(x_arr, y_arr, color="yellow")

y_arr = bin_to_list(bin(input_list[1]))
plt.subplot(232)
plt.title("param2")
plt.plot(x_arr, y_arr, color="red")

y_arr = bin_to_list(bin(input_list[2]))
plt.subplot(233)
plt.title("param3")
plt.plot(x_arr, y_arr, color="blue")

y_arr = bin_to_list(bin(check_sum(input_list)))
plt.subplot(2, 1, 2)
plt.title("checkSum")
plt.plot(x_arr, y_arr, color="green")
plt.savefig('checkSum', bbox_inches='tight')
plt.show()
