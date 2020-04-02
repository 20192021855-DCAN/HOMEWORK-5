import numpy as np
def getChecksum(nums: list) -> int:
 val = 0
 maximum = pow(2, 16)
 for num in nums:
  val += int(num, 2)
 if val >= maximum :
  val = val % maximum + val / maximum
 return int(val)
 if __name__ == "__main__":
  nums = ['0110011001100000', '0101010101010101', '1000111100001100']
 checksum = ~getChecksum(nums)
 print("校验和：" + np.binary_repr(checksum, width=16))
 print("接受方处和: 1111111111111111.")