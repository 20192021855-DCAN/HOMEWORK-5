#copyright: 2017302580026 Ö£»Û
from matplotlib import pyplot as plt 

def check_draw(data):
    sum = 0
    x = []
    y = []
    for i in range(0,len(data),4):
        val = int(data[i:i+4],16)
        sum = sum + val
        y.append(bin(sum))
        
    while sum > 0xffff:
        sum = (sum>>16)+(sum&0xffff)
        y.append(bin(sum))
    res = sum^0xffff
    y.append(bin(res))
   
    for i in range(1,len(y)+1):
        x.append(i)
    plt.title("Process Display") 
    plt.xlabel("Step") 
    plt.ylabel("bit value")
    plt.bar(x, y)
    return bin(res)

a = '666055558f0c'
print("¼ìÑéºÍÎª£º" + (check_draw(a)))