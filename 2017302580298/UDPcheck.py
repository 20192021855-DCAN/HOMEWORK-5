import numpy as np
from matplotlib import pyplot as plt

data=np.array([0b0110011001100000,0b0101010101010101,0b1000111100001100])

def check (a):
    n = a.size
    sum = 0
    for items in a:
        sum = add(sum,items)
    return sum

def add (a,b):
    sum = a + b
    carray = (sum & 0x00010000)>>16
    if carray==1 :
        sum = sum & 0x0000ffff
        sum = add(sum,1)
    return sum

def display():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('UDPcheck', fontsize=12, fontweight='bold')
    ax.axis([0, 10, 0, 10])
    temp = add(data[0],data[1])
    # data[0] data[1]
    ax.text(3, 9, bin(data[0])[2:].zfill(16), fontsize=14)
    ax.text(3, 8, bin(data[1])[2:].zfill(16), fontsize=14)
    ax.text(0.5, 7.5, "____________________________________________________________", fontsize=10)
    ax.text(3, 6.5, bin(temp)[2:].zfill(16), fontsize=14, color="green")
    # data[2]
    ax.text(3, 5.5, bin(data[2])[2:].zfill(16), fontsize=14)
    ax.text(0.5, 5, "____________________________________________________________", fontsize=10)
    ax.text(3, 4, bin(add(temp,data[2]))[2:].zfill(16), fontsize=14, color="green")
    # final result
    ax.text(0.5, 3.5, "____________________________________________________________", fontsize=10)
    ax.text(3, 2.5, bin(sum)[2:].zfill(16), fontsize=14, color="red")
    plt.show()

sum = check(data)
sum = (~sum&(0xffff))
print(bin(sum))
display()

