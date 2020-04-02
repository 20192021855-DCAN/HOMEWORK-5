import re

def cal(strs):
    # 输入参数的检查
    assert (type(strs) == list) ,"输入参数必须为字符串列表"
    # 用正则检查数组中每个参数是否符合要求
    assert (len(list([s for s in strs if re.match("(0|1){16}",s) != None])) == len(strs)),"输入二进制串有误"
    res  = 0
    for s in strs:
        res += int(s,2)
        res = (res & 0xffff) + (res >> 16)
    res ^= 0xffff
    return bin(res).replace("0b","")

if __name__ == '__main__':
    input_strs = ["0110011001100000",
                     "0101010101010101",
                     "1000111100001100"]
    print("输入的二进制数字为："+str(input_strs))
    print("校验和为："+cal(["01011100","01100101"]))