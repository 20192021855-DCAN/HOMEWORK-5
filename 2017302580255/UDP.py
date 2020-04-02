n = eval(input("请输入n:"))
x = []
for i in range(n):
    x.append(eval("0b" + input("请输入16位比特数：")))
sum_total = sum(x)
y = sum_total >> 16
while y != 0:
    sum_total_str = str(bin(sum_total))
    sum_total_lower = eval("0b"+sum_total_str[-16:])
    sum_total = sum_total_lower + y
    y = sum_total >> 16

result = str(bin(65535 - sum_total))[2:]
print(result)





