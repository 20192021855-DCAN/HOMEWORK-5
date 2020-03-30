
#-get checksum of UDP segement
#-param: 
#   @data1 - [int] ; >=0 ; binary length must less than or equal to @n
#   @data2 - same as data1
#   @data3 - same as data1
#   @n     - [int] ; > 0 ; limitation of binary length
#-return == -1 [param error]
#        >=  0 [  normal   ]
def checksum(data1, data2, data3, n):
    # confirm the params
    if(data1 < 0 or data2 < 0 or data3 < 0 or n <= 0
    or data1.bit_length() > n or data2.bit_length() > n
    or data3.bit_length() > n):
        return -1
    # calculate the ckecksum
    tmp = data1 + data2
    if(tmp.bit_length() > n):
        tmp = tmp - 2**n + 1
        if(tmp.bit_length() > n):
            tmp = tmp - 2**n + 1
    tmp += data3
    if(tmp.bit_length() > n):
        tmp = tmp - 2**n + 1
        if(tmp.bit_length() > n):
            tmp = tmp - 2**n + 1
    return 2**n - (1+tmp)

data1 = int(input("type in the first data: "), 2)
data2 = int(input("type in the second data: "), 2)
data3 = int(input("type in the third data: "), 2)
result= checksum(data1,data2,data3,16)
if(result < 0):
    print("error input!")
else:
    print("the UDP checksum is:", bin(result)[2:])