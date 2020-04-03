import matplotlib.pyplot as plt

# ����16λ����
a = '1000100010001000'
b = '1100110011001100'
temp_a = a
temp_b = b

# ת��Ϊʮ���ƺ����
# �������ַ���ת��Ϊ����
a = int(a)
b = int(b)
# ���������ת��Ϊʮ���ƺ��ֵ
decimal_a = 0
decimal_b = 0
i = 0
while a:
    dec = a % 2  # ȡ�����һ������
    decimal_a += dec * pow(2, i)  # ��ÿһλ������������λȨ��ˣ�Ȼ����Ӿ͵õ���ʮ������
    a = a // 10  # ����������������������֣���ȥ���һλ
    i += 1
i = 0
while b:
    dec = b % 2
    decimal_b += dec * pow(2, i)
    b = b // 10
    i += 1
sum_ab = decimal_a + decimal_b
flag = 0
wrap_sum_ab = sum_ab
# �ж��Ƿ�ؾ�
if sum_ab >= 65536:
    flag = 1
    wrap_sum_ab = sum_ab - 65535
# ��
checksum = (~wrap_sum_ab) & 0xffff
# ����ͽ����ʮ������ת��Ϊ�����ƣ�չʾ��Ҫ��ֱ����У��Ͳ���Ҫ��
temp = []
result = ''
# շת�����
while sum_ab:
    dec = sum_ab % 2
    sum_ab = sum_ab // 2
    temp.append(dec)
# ��Ϊ��շת�����������˳��Ҫ�෴
while temp:
    result += str(temp.pop())
result = int(result)
# �ѻؾ�����ʮ������ת��Ϊ������
temp = []
wrap_result = ''
while wrap_sum_ab:
    dec = wrap_sum_ab % 2
    wrap_sum_ab = wrap_sum_ab // 2
    temp.append(dec)
while temp:
    wrap_result += str(temp.pop())
wrap_result = int(wrap_result)
# ���󷴽����ʮ������ת��Ϊ������
temp = []
checksum_result = ''
while checksum:
    dec = checksum % 2
    checksum = checksum // 2
    temp.append(dec)
while temp:
    checksum_result += str(temp.pop())
checksum_result = int(checksum_result)


fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=2)
ax.set_title('checksum', fontsize=18, fontweight='bold')
ax.axis([0, 10, 0, 10])

# ����˵��
ax.text(0.5, 9, 'step 1: add two binary integers', style='italic',
        bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 10})
ax.text(0.5, 5, 'step 2: wrap the carry and add it to low order bit', style='italic',
        bbox={'facecolor': 'yellow', 'alpha': 0.5, 'pad': 10})
ax.text(0.5, 1, 'step 3: checksum is the complement code', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

# ��������ͽ����ʾ
ax.text(6, 9, temp_a, fontsize=15)
ax.text(6, 8, temp_b, fontsize=15)
ax.text(5.8, 7, result, fontsize=15)

# �ؾ�����ʾ
ax.annotate('carry-over', xy=(5.8, 7.2), xytext=(4, 7.3),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('wrap', xy=(9.3, 4.1), xytext=(6, 6.5),
            arrowprops=dict(facecolor='red'))
ax.text(9.5, 4, flag, fontsize=15)
ax.text(6.2, 3, wrap_result, fontsize=15)

# ��
ax.text(6, 1, checksum_result, fontsize=15)



plt.show()