def udpcheck(list):
    addnum = 0
    for i in range(0,list.__len__()):#得到相加的和
        if list[i].__len__() != 16:
            print("长长长the length not 为16")
            break
        addnum += int(list[i],2)#这数组中的数字依次相加
        if addnum > 65535:
            addnum = addnum - 65536 + 1 #回卷
    checksum = 65535 - addnum #得到反码吗码ma
    sum = checksum
    for i in range(0,list.__len__()):
        sum += int(list[i],2)
        if sum > 65535:
            sum = sum - 65536 + 1
    print("sum的值value为="+bin(sum).__str__())
    if sum == 65535:
        print("true")
    else:
        print("false")


testlist = ["0110011001100000", "0101010101010101", "1000111100001100"]
udpcheck(testlist)
