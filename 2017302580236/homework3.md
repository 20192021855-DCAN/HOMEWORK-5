### P3

计算过程如下：

```
   1 0 1 1 1 0 0 1
 + 0 1 1 0 0 1 1 0
------------------
   0 1 0 1 0 0 1 1


   0 1 1 1 0 1 0 0
 + 1 0 1 1 1 0 0 1
 -----------------
   0 0 1 0 1 1 1 0
```

补码为： 1 1 0 1 0 0 0 1

为了检测错误，接收方添加四个单词(三个原始单词和校验和)。如果和包含一个零，接收器知道有一个错误。所有的一位错误都会被检测到，但是两位错误可以不被检测到(例如，如果第一个单词的最后一个数字被转换为0，第二个单词的最后一个数字被转换为1)。

### P4

a. 相加得到11000001，取反得00111110.

b. 相加得到01000000，补码为10111111.

c.第一个字节=01010100；第二个字节=01101101.

### UDP16位校验和

![](E:\本科学习\lessons\大三下\网络及分布式\homework\2017302580236\UDP.png)

​                                                                                              ***2017302580236 刘一婧*** 