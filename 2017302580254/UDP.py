import numpy as np 

def checksum(data_list): 
    answer = 0 
    for x in data_list: 
    answer += x 
    if answer > 0xffff: 
    answer = (answer & 0xffff) + 1 

answer = answer ^ 0xffff 
return answer 

 
if __name__ == '__main__': 
data_list = [int('0110011001100000', 2), int('0101010101010101', 2), int('1000111100001100', 2)] 
result = checksum(data_list) 
print("real_answer:1011010100111101") 
print("check_answer:" + np.binary_repr(result)) 
print("1011010100111101".__eq__(np.binary_repr(result))) 