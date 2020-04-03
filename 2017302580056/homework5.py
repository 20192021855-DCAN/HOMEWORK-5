import matplotlib.pyplot as plt

import numpy as np

import sys



def checkSum(mylist):

    sum=0;

    for i in range(0,2):
        sum=mylist[i]+mylist[i+1];
        if sum > pow(2,16):
            sum-=pow(2,16);
            sum+=1;
    sum = pow(2,17)-sum-1;
    return sum




mylist=[0b0110011001100000,0b0101010101010101,0b1000111100001100]
checksum=checkSum(mylist)
print("校验和："+bin(checksum).__str__()[3:])

