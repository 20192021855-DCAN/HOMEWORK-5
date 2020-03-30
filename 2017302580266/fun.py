# 获取输入
input1 = input("输入：")
input2 = input("输入：")
input3 = input("输入：")
if len(input1) == 16 and  len(input2) == 16 and  len(input3) == 16:
    try:
        # 转为十进制
        input1 = int(input1,2)
        input2 = int(input2,2)
        input3 = int(input3,2)
        # 求和
        add_12 = str(bin(input1+input2))
        # 进位则回卷
        if(len(add_12)>18):
            add_12 = int(add_12[3:],2)+1
        else:
            add_12 = int(add_12,2)
        # 求和
        add_123 = str(bin(add_12+input3))
        # 进位则回卷
        if(len(add_123)>18):
            add_123 = int(add_123[3:],2)+1
        else:
            add_123 = int(add_123,2)
        add_123 = str(bin(add_123))[2:]
        result = ""
        # 补齐16位
        while len(add_123)!=16:
            add_123 = "0"+add_123
        # 获得反码
        for i in add_123:
            if i=="0":
                result+="1"
            else:
                result+="0"
        print("结果如下")
        print(result)
    except Exception:
        print("input error")
else:
    print("too short or too long")