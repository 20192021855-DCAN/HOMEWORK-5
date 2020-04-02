import numpy as np
from matplotlib import pyplot as plt

data = ["0110011001100000","0101010101010101","1000111100001100"]
sum = 0
max_num = pow(2, 16)
for i in data:
    sum += int(i, 2)
    sum = (sum % max_num) + (sum // max_num)
print("和：{}".format(sum))
checksum = np.binary_repr(~sum, width=16)
print("校验和：{}".format(checksum))

x, y = range(1,17),list(map(int,list(data[0])))
plt.plot(x, y, "r",label='0110011001100000')
x, y = range(1,17),list(map(int,list(data[1])))
plt.plot(x, y, "g",label='0101010101010101')
x, y = range(1,17),list(map(int,list(data[2])))
plt.plot(x, y, "b",label='1000111100001100')
x, y = range(1,17),list(map(int,list(str(checksum))))
plt.plot(x, y, "black",label='checksum')
plt.legend(loc="lower right")
plt.show()
