import numpy as np

def udp(nums: list):
    sum = 0             
    maximum = pow(2, 16)  
    for num in nums:
        sum += int(num, 2)
        if sum >= maximum :
            sum = (sum & 0xffff) + 1
    return ~sum

if __name__ == "__main__":
    nums = ['0110011001100000', '0101010101010101', '1000111100001100']
    checksum = udp(nums)
    print("校验和：" + np.binary_repr(checksum, width=16))