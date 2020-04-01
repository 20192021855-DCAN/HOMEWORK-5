import numpy as np



dataArr=[]
def generateChecksum(arr):
    sum=0
    for item in arr:
        sum=sum+item
    while(sum>>16):
        sum=(sum>>16)+(sum&0b1111111111111111)
    return '{:0>16b}'.format((~sum)&0b1111111111111111)

if __name__ == "__main__":
    dataArr.append(0b1110011001100110)
    dataArr.append(0b1101010101010101)
    print(generateChecksum(dataArr))
    