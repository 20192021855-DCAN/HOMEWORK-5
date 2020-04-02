#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt  # 为方便简写为plt

class JudgeRecCode:
    def judge(self, s1, s2, s3):
        # 将字符串转Int
        num1 = int(s1, 2);
        num2 = int(s2, 2);
        num3 = int(s3, 2);
        # 将三个二进制进行累加
        c = bin(num1 + num2 + num3);
        result = c[2:];
        print(result);
        plt.text(2.5, n-5, "----------------------------------");
        plt.text(-0.1, n - 5, "Step1:Sum numbers", color='blue');
        plt.text(2.1, n-6, "result:" + str(result));
        # 如果结果的长度大于17，则证明需要回卷
        length = len(result);
        plt.text(-0.1, n - 7, "Step2:Judge length", color='blue');
        while (length >= 17):
            plt.text(2.2, n-7, "length>=17,need rollback",color='red');
            nowResult = result[1:];
            nowNum = int(str(nowResult), 2);
            addNum = int("1", 2);
            newResult = bin(nowNum + addNum)[2:];
            length = len(newResult);
            result = newResult;
        #如果长度不足16，进行0补码
        while length < 16:
            finalStr = "0" + str(result);
            length = length + 1;
        #输出最终计算结果：
        plt.text(1.7, n-8, "final result:"+finalStr);
       #进行反码操作
        ComStr = "";
        for f in finalStr:
            if (int(f) == 0):
                ComStr = ComStr + "1";
            else:
                ComStr = ComStr + "0";
        #输出最终反码结果
        plt.text(-0.1, n - 9, "Step3:Inverse", color='blue');
        plt.text(1.5, n-9, "inverse code:" + ComStr);



if __name__ == "__main__":
    #确定输入计算的三个字符串
    s1 = "0110011001100000";
    s2 = "0101010101010101";
    s3 = "1000111100001100";
    jd = JudgeRecCode();
    plt.figure();
    #规定坐标的x y轴大小范围
    plt.xlim(-1, 7)
    plt.ylim(0, 13)
    n=13;
    plt.text(2.5,n-2,"    "+s1);
    plt.text(2.5, n-3, "+ "+s2);
    plt.text(2.5, n-4, "+ "+s3);

    jd.judge(s1, s2, s3);
    plt.show();
