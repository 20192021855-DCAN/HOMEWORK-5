def checkSum(data):
    ans = data[0] + data[1]
    ans = (ans & 0xFFFF) + (ans >> 16)
    ans = ans + data[2]
    ans = (ans & 0xFFFF) + (ans >> 16)
    return ~ans


if __name__ == '__main__':
    checksum = 0b1011010100111101
    data = [0b0110011001100000, 0b0101010101010101, 0b1000111100001100]
    ans = checkSum(data)
    print("数组：1、",bin(data[0])[2:].zfill(16)," 2、",bin(data[1])[2:].zfill(16)," 3、",bin(data[2])[2:].zfill(16))
    print("实际校验和：",bin(checksum)[2:].zfill(16))
    print("求得校验和：",bin(ans)[2:].zfill(16))
    if ans == checksum:
        print("校验结果：正确")
    else:
        print("校验结果：错误")
    input()
