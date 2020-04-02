import numpy as np

def checkSum(data_list):
    checkSumResult= 0
    for x in data_list:
        # 求和
        checkSumResult += x
        # 回卷
        if checkSumResult > 0xffff:
            checkSumResult = (checkSumResult & 0xffff) + 1
    # 结果取反得校验和
    checkSumResult = checkSumResult ^ 0xffff
    return checkSumResult

def checkTheAnswer(checkSumResult,datalist):
    for x in datalist:
        checkSumResult+=x;
    if checkSumResult > 0xffff:
        checkSumResult = (checkSumResult & 0xffff) + 1
    if checkSumResult == 0xffff:
        print('true')
    else:
        print('false')

if __name__ == '__main__':
    datalist=[int('0110011001100000',2), int('0101010101010101',2), int('1000111100001100',2)] #二进制表示的字符串转化为int型
    checkTheAnswer(checkSum(datalist),datalist)