import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
x = 0b0110011001100000
y = 0b0101010101010101
z = 0b1000111100001100
result = x + y
if result >> 16 > 0:
    result = (result & 0xffff) + 0x1
result += z
if result >> 16 > 0:
    result = (result & 0xffff) + 0x1
print('反码前：' + bin(result)[2:].zfill(16))
result1 = bin(result)[2:].zfill(16)
result = result ^ 0xffff
print('反码后：' + bin(result)[2:].zfill(16))
result = bin(result)[2:].zfill(16)
# 设置颜色
if __name__ == '__main__':
    str1 = "0110011001100000"
    str2 = "0101010101010101"
    str3 = "1000111100001100"
    data1 = [list(map(int, str1))]
    data2 = [list(map(int, str2))]
    data3 = [list(map(int, str3))]
    data4 = [list(map(int, result1))]
    data5 = [list(map(int, result))]
    fig = plt.figure()
    cdict = ['#000000', '#FFFFFF']
    my_cmap = colors.ListedColormap(cdict, 'indexed')
    # 绘图
    ax1 = fig.add_subplot(421)
    ax1.imshow(data1, cmap=my_cmap)
    ax1.set_xticks(np.arange(16))
    ax1.set_ylabel("data1")
    ax1.set_yticks([])
    ax2 = fig.add_subplot(422)
    ax2.imshow(data2, cmap=my_cmap)
    ax2.set_xticks(np.arange(16))
    ax2.set_ylabel("data2")
    ax2.set_yticks([])
    ax3 = fig.add_subplot(423)
    ax3.imshow(data3, cmap=my_cmap)
    ax3.set_xticks(np.arange(16))
    ax3.set_ylabel("data3")
    ax3.set_yticks([])
    ax4 = fig.add_subplot(424)
    ax4.imshow(data4, cmap=my_cmap)
    ax4.set_xticks(np.arange(16))
    ax4.set_ylabel("before")
    ax4.set_yticks([])
    ax5 = fig.add_subplot(425)
    ax5.imshow(data5, cmap=my_cmap)
    ax5.set_xticks(np.arange(16))
    ax5.set_ylabel("after")
    ax5.set_yticks([])
    plt.show()