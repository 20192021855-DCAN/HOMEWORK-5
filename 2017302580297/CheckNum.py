import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def colormap():
    cdict = ['#FFFFFF', '#000000']
    return colors.ListedColormap(cdict, 'indexed')


def checksum(data):
    sum = 0
    index = 0
    while index < len(data):
        a = int(data[index:index + 16], 2)
        sum = int(str(sum),2)
        sum = bin(sum + a)[2:]
        while(len(sum) > 16):
            sum = int(sum, 2) - pow(2, len(sum) - 1)
            sum = bin(sum + 1)[2:]
        index += 16

    result = str(sum)
    while len(result) < 16:
        result = '0' + result

    result = list(result)
    for i in range(len(result)):
        if result[i] == "1" : result[i] = "0"
        elif result[i] == "0" : result[i] = "1"
    result = ''.join(result)
    print("校验和为：" + result)
    return result

if __name__ == '__main__':

    str1 = "0110011001100000"
    str2 = "0101010101010101"
    str3 = "1000111100001100"

    data1 = [list(map(int, str1))]
    data2 = [list(map(int, str2))]
    data3 = [list(map(int, str3))]

    data4 = [list(map(int, checksum(str1 + str2 + str3)))]

    fig = plt.figure()
    my_cmap = colormap()

    ax1 = fig.add_subplot(411)
    ax1.imshow(data1, cmap=my_cmap)
    ax1.set_xticks(np.arange(16))
    ax1.set_ylabel("data1")
    ax1.set_yticks([])

    ax2 = fig.add_subplot(412)
    ax2.imshow(data2, cmap=my_cmap)
    ax2.set_xticks(np.arange(16))
    ax2.set_ylabel("data2")
    ax2.set_yticks([])

    ax3 = fig.add_subplot(413)
    ax3.imshow(data3, cmap=my_cmap)
    ax3.set_xticks(np.arange(16))
    ax3.set_ylabel("data3")
    ax3.set_yticks([])

    ax4 = fig.add_subplot(414)
    ax4.imshow(data4, cmap=my_cmap)
    ax4.set_xticks(np.arange(16))
    ax4.set_ylabel("result")
    ax4.set_yticks([])

    plt.show()
