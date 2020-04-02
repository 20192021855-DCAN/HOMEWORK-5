def check(datas):
    _sum=0
    for _data in datas:
        _sum=_data+_sum
    _sum=displacement(_sum)
    _sum ^= 0xffff
    return _sum
def displacement(data):
    while True:
        _low = data & 0xffff
        _high = data >> 16
        if _high>0:
            data=_low+_high
        else:
            return data


datas = [0b0110011001100000, 0b0101010101010101, 0b1000111100001100]
if __name__ == '__main__':
    sum=check(datas) + datas[0] + datas[1] + datas[2]
    sum=displacement(sum)
    if  sum== 0xffff:
        print('校验结果正确')
    else:
        print('校验结果失败')


