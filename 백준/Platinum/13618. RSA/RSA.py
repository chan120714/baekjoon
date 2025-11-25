from math import gcd
from random import*
p=[2,3,5,7,11,13,17,19,23,29,31,37,41]

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

n,e,c=map(int,input().split())

q=rho(n)
P=n//q
d=pow(e,-1,(P-1)*(q-1))
print(pow(c,d,n))