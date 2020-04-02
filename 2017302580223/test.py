data=[
    0b0110011001100000,
    0b0101010101010101,
    0b1000111100001100
]

def check(data):
    sum=0
    for item in data:
        last=sum
        sum+=item
        print(dem2(sum)+" = "+dem2(last)+" + "+dem2(item))
        if(sum>0xffff):
            print(dem2(sum)+" > "+"0xffff")
            sum=(sum&0xffff)+1
            print(dem2(sum))
    sum=sum^0xffff
    print(dem2(sum))
    return sum

def add_check(data):
    sum=check(data)
    for item in data:
        sum+=item
    print(dem2(sum))


def dem2(num):
    res=""
    for i in range(0,16):
        n=num%2
        res=str(n)+res
        num//=2
    if res=="":
        res="0000000000000000"
    return res

add_check(data)
