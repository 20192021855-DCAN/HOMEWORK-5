~~~ python
import re

def udp(strs):
    #使用正则表达式判断
    assert (type(strs) == list) ,"输入参数必须为字符串列表"
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
    print("校验和为："+udp(input_strs))
~~~
