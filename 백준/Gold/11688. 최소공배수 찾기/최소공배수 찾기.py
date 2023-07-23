from math import *
n,m,k=map(int,input().split())
a=[]
c=[]
for i in range(1,int(sqrt(k))+1):
    if k%i==0:
        a.append(i)
        c.append(k//i)
q=n*m//(gcd(n,m))
for i in a:
    t=gcd(q,i)
    if k==q*i//t:
        print(i)
        exit()
c.reverse()
for i in c:
    t=gcd(q,i)
    if k==q*i//t:
        print(i)
        exit()
print(-1)