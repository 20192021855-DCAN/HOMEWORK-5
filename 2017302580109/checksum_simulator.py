import random
import matplotlib.pyplot as plt
import numpy as np

def compute_checksum():
	#随机生成两个十六进制整数，实际映射为-2^15 ~ 2^15 - 1
	lower_limit = -2**15
	upper_limit = 2**15 - 1
	integer_1 = random.randint(lower_limit, upper_limit)
	integer_2 = random.randint(lower_limit, upper_limit)
	initial_sum = integer_1 + integer_2
	##模拟回卷：若超过16位，则回卷
	if(initial_sum > upper_limit):
		initial_sum = initial_sum - 2**15 + 1 ##去掉首位，并加回个位
	checksum = initial_sum
	#和如果是负数，还需要取补码，并且求反
	if(checksum < 0):
		checksum = (checksum & 0xffff)
	return [integer_1, integer_2, bin(checksum).replace("0b", "").replace("0", "a").replace("1", "0").replace("a", "1")]

def transform_integer_into_bit_list(integer):
	cpl_code = integer
	if(integer < 0):
		cpl_code = cpl_code & 0xffff
	bit_list = list(bin(cpl_code).replace("0b", ""))
	if len(bit_list) < 16:
		for i in range(0, 16 - len(bit_list)):
			bit_list.insert(0, '0') #补全高位的0
	return bit_list


def plot_illustration():
	[integer_1, integer_2, checksum] = compute_checksum()
	#绘制两个子图，第一张图显示两个整数的位信息，第二张图显示最后的checksum信息，折线图表示
	fig = plt.figure()
	x_axis = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
	int_1_bit_list = transform_integer_into_bit_list(integer_1)
	int_2_bit_list = transform_integer_into_bit_list(integer_2)
	checksum_list = list(checksum)
	if len(checksum_list) < 16:
		for i in range(0, 16 - len(checksum_list)):
			checksum_list.insert(0, '0') #补全高位的0

	ax_1 = fig.add_subplot(121)
	ax_1.plot(x_axis, int_1_bit_list,c='#00CED1',marker='o',markeredgewidth=1,markeredgecolor='w',linestyle='-.',  linewidth=2, markersize=7, label="1st integer",)
	ax_1.plot(x_axis, int_2_bit_list,c='#FF6347',marker='*',linestyle=':',  linewidth=2, markersize=7, label="2nd integer")
	ax_1.set_xticks(x_axis)
	ax_1.set_xlabel('Bit Rank')
	ax_1.set_ylabel('Bit Value')
	ax_1.set_title("Bit Pattern of 1st and 2nd integer")
	leg = plt.legend()
	ax_2 = fig.add_subplot(122)
	ax_2.plot(x_axis, checksum_list,  c='#BA55D3',marker='p',linestyle='--',  linewidth=2, markersize=7, label="checksum")
	ax_2.set_xticks(x_axis)
	ax_2.set_xlabel('Bit Rank')
	ax_2.set_ylabel('Bit Value')
	ax_2.set_title("Bit Pattern of checksum")
	leg = plt.legend()
	plt.show()

plot_illustration()