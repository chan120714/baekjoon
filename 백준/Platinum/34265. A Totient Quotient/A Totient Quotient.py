from collections import defaultdict
from math import gcd
from random import*
p=[2,3,5,7,11,13,17,19,23,29,31,37,41]

def pow(x,y,p):
    if y<2:
        return (x**y)%p
    if y%2:
        return (pow(x,y//2,p)**2*x)%p
    return (pow(x,y//2,p)**2)%p

def mil(n,a):
    s,d=0,n-1
    while d%2==0:
        s+=1
        d//=2
    x=pow(a,d,n)
    if x==1 or x+1==n:
        return True
    for i in range(s-1):
        x=pow(x,2,n)
        if x+1==n:
            return True
    return False

def pri(n):
    if n in p: return True
    if n==1 or n%2==0: return False
    for k in p:
        if not mil(n,k):return False
    return True

def rho(n):
    if pri(n):return n
    if n==1:return 1
    if n%2==0:return 2
    x,c,d=randint(2,n-1),randint(1,n-1),1
    y=x
    while d==1:
        x=(x**2+c)%n
        y=(y**2+c)%n
        y=(y**2+c)%n
        d=gcd(n,abs(x-y))
        if d==n: return rho(n)
    if pri(d): return d
    return rho(d)

def phi(x):
    res=x
    while x>1:
        t=rho(x)
        while x%t==0:
            x//=t
        res*=t-1
        res//=t
    return res

a,b=map(int,input().split())
n=[0]*10121
m=[0]*10121
res1,res2=1,1
while a>1:
    k=rho(a)
    n[k]+=1
    a//=k

while b>1:
    k=rho(b)
    b//=k
    m[k]+=1


for i in range(10000,1,-1):
    
    k=min(n[i],m[i])
    n[i]-=k
    m[i]-=k
    
    if n[i]>m[i]:
        t=n[i]
        if t%2:
            res2*=i**((t-1)//2+1)
            i-=1
            while i>1:
                t=rho(i)
                m[t]+=1
                i//=t
        else:
            res1*=i
            res2*=i**(1+t//2)
    elif n[i]<m[i]:
        t=m[i]
        if t%2:
            res1*=i**((t-1)//2+1)
            i-=1
            while i>1:
                t=rho(i)
                n[t]+=1
                i//=t
        else:
            res2*=i
            res1*=i**(1+t//2)
print(res2,res1)