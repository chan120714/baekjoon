from math import gcd

w,h,l1,l2=map(int,input().split())


res=0

for i in range(1,w+1):
    for j in range(1,h+1):
        if gcd(i,j)==1 and l1**2<=i**2+j**2<=l2**2:
            res+=(w-i+1)*(h-j+1)*2
if l1<=1<=l2:
    res+=w*h*2+w+h
print(res)
