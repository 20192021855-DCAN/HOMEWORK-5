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