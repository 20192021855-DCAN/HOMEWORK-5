
# datas 为UDP报文段16比特字数组
def checksum (datas):
    ans = 0b0
    for data in datas:
        print("current 16 bits word : " + bin(data)[2:].zfill(16))
        ans += data
    print("未经过溢出检查的检验和：" + bin(ans)[2:].zfill(16))
    while True:
        low = ans & 0xffff
        high = ans >> 16

        if high > 0:
            # 需要回卷
            ans = low + high
        else:
            print("经过检验和回卷处理结果: " + bin(ans)[2:].zfill(16))
            ans ^= 0xffff
            print("经过检验和取反处理结果: " + bin(ans)[2:].zfill(16))
            return ans


if __name__ == '__main__':
    datas = [0b0110011001100000,
             0b0101010101010101,
             0b1000111100001100]
    ans = checksum(datas)
    print("UDP检验和计算结果:     " + bin(ans)[2:].zfill(16))



