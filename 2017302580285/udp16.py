import struct
 
 
def check(data):
    sum=0
    for i in range(0,len(data),16):
        val = int(data[i:i+16],2)
        sum = sum + val
        sum = sum & 0xffffffff 
    sum = (sum >> 16) + (sum & 0xffff)
    if sum > 65535:
        sum = (sum >> 16) + (sum & 0xffff)
    return 65535-sum
a= '11100110011001101101010101010101' 
udp_check = check(a)
sum=0
for i in range(0,len(a),16):
        val = int(a[i:i+16],2)
        sum = sum + val
        sum = sum & 0xffffffff
sum = (sum >> 16) + (sum & 0xffff)
udp_check += sum

print('udp_check:',hex(udp_check))