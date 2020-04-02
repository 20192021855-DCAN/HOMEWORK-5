import matplotlib
from matplotlib import pyplot as plt

def _sum(data_1,data_2,data_3):
    temp = data_1+ data_2
    temp = (temp&0xFFFF) + (temp>>16)
    temp = temp + data_3
    temp = (temp & 0xFFFF) + (temp >> 16)
    return temp

if __name__ == '__main__':

    #  0b 表示是 二进制表示
    data_1 = 0b0110011001100000
    data_2 = 0b0101010101010101
    data_3 = 0b1000111100001100
    # 三个字的“和”
    temp = _sum(data_1,data_2,data_3) 
    # 检验和，与按位取反等效
    checkSum = temp^0xFFFF
    #  zfill(length) 在length的长度里从左往右自动补零（0b不再出现）
    print("3个16比特字的和： "+ bin(temp)[2:].zfill(16))
    print("取反得到的校验和：" + bin(checkSum)[2:].zfill(16))
    print("全部的4个16比特字加在一起：" + bin(temp+checkSum)[2:].zfill(16))

    # 画图 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('checksum', fontsize=12, fontweight='bold')
    ax.axis([0, 6, 0, 6])
    # 过程
    ax.text(0.5, 5.5, "word 1 :", fontsize=14)
    ax.text(3, 5.5, bin(data_1)[2:].zfill(16), fontsize=14)
    ax.text(0.5, 5, "word 2 :", fontsize=14)
    ax.text(3, 5, bin(data_2)[2:].zfill(16), fontsize=14)
    #  第一个和
    ax.text(0.5, 4.9, "____________________________________________________________", fontsize=10)
    ax.text(3, 4.5, bin(data_1+data_2)[2:].zfill(16), fontsize=14,color="green")
    ax.text(0.5, 4, "word 3 :", fontsize=14)
    ax.text(3, 4, bin(data_3)[2:].zfill(16), fontsize=14)
    #  第二个和
    ax.text(0.5, 3.9, "____________________________________________________________", fontsize=10)
    ax.text(3, 3.5, bin(temp-1)[2:].zfill(16), fontsize=14,color="green")
    ax.text(2.85, 3.5, "1", fontsize=14,color="red")
    #  需要回卷
    ax.text(3, 2.75, bin(temp-1)[2:].zfill(16), fontsize=14,color="green")
    ax.text(5.25, 2.35, "1", fontsize=14,color="green")
    ax.text(0.5, 2.25, "____________________________________________________________", fontsize=10)
    # 3个16比特的字 的“和”
    ax.text(0.5, 1.75, "sum of 3 words :", fontsize=14)
    ax.text(3, 1.75, bin(temp)[2:].zfill(16), fontsize=14)
    # 校验和
    ax.text(0.5, 1, "checkSum :", fontsize=16)
    ax.text(3, 1, bin(checkSum)[2:].zfill(16), fontsize=14)
   
    plt.show()


  
 
   