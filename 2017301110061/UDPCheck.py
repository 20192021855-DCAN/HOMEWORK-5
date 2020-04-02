def CheckSum(list):
    sum=0
    for l in list:#对list中每个16位数
        if len(l)!=16:
            print("数据来源中某项不为16位，请检查数据")
            return -1#错误时返回-1
        sum+=int(l,2)#将每个16位数转化为10进制数然后再加减
        sum=(sum&0xffff)+(sum>>16)#回卷运算
    return sum^(0xffff)#取反返回

if __name__=='__main__':
    list=["0110011001100000",
          "0101010101010101",
          "1000111100001100"]
    actSum="1011010100111101"
    calSum=bin(CheckSum((list))).replace("0b","")#将获得的校验和转化为2进制并删除开头
    for i in range(0,len(list)):
        print("第"+str(i+1)+"个16位数字是"+list[i])
    print("预测校验和是"+calSum)
    print("真实检验和是"+actSum)
    if actSum==str(calSum):
        print("预测值和真实值相等")
    else:
        print("预测值和真实值不等")

