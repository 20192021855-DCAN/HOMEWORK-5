## UDP校验和计算

1. 代码

   ```py
   import numpy as np
   content1=input()
   content2=input()
   ans=int(content1)+int(content2)
   if (ans>1111111111111111):
     result=((int(content1,2)+int(content2,2))&0xffff)+1
   else:
     result=(int(content1,2)+int(content2,2))&0xffff
   result=~result
   print("校验和为"+np.binary_repr(result&0xffff,16))
   ```

2. 运行截图![运行截图](/img/1.png)

## 习题

### P4

1. 01011100+01100101=11000001 

   反码为00111110

2. 11011010+01100101=1001111111

   回卷结果为01000000

   反码为10111111

3. 两个字节分别变为01111100和01000101

### P22

1. 接受方期待的有序分组序号为K，说明接收方已经接受到了K-1分组，并发送了ACK(k-1),有两种边界情况——得出分组序号为k-4~k+3
   + 接收方在等待ACK(k-1),此时窗口位于[k-4,k-1]
   + 接收方接受到ACK(k-1),此时窗口向前滑动，位于[k,k+3]
2. 接收方还未接收到K，因此ACK字段范围为k-4~k-1