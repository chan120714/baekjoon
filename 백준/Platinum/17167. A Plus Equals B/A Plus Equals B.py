from math import *
a,b=map(int,input().split())
c=gcd(a,b)
a//=c
b//=c
d=[]
while True:
    if a==1 and b==1:
        break
    while a%2==0:
        d.append("B+=B")
        a//=2
    while b%2==0:
        d.append("A+=A")
        b//=2
    if a%2==1 and b%2==1:
        if a<b:
            d.append("B+=A")
            b+=a
            d.append("A+=A")
            b//=2
        if b<a:
            d.append("A+=B")
            a+=b
            d.append("B+=B")
            a//=2
    c=gcd(a,b)
    a//=c
    b//=c
print(len(d))
for i in range(len(d)):
    print(d[i])