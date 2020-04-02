
from matplotlib import pyplot as plt

class udp:

    def checkSum(self,source_array):
        """
        UDP的16位校验和
        :param source_array: 输入的16位集
        :return:校验和
        """
        length = len(source_array)
        sum = [0]*length
        if length<2:
            return
        for count in range(length-1):
            if count == 0:
                sum[0] = source_array[0] + source_array[1]
            else:
                sum[count] = sum[count-1]+source_array[count+1]
                while sum[count]>0xffff:
                    sum[count] = (sum[count] & 0xffff) + 1
        sum[length-1] = (~sum[length-2]) & 0xffff
        return sum
    def show(self,names,values):

        plt.plot(names, values)
        plt.title('Decimal System Bar Graph')
        plt.ylabel('the process of sum')
        plt.xlabel('16 bit word')
        plt.show()


if __name__ == '__main__':
    a = udp()
    name = [0b0110011001100000,0b0101010101010101,0b1000111100001100]
    result = a.checkSum([0b0110011001100000,0b0101010101010101,0b1000111100001100])
    for b in result:
        print(b)
    #name值用string类型代替
    a.show(["26208","21845","36620"], result)

