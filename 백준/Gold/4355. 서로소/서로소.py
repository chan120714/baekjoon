import sys
input=sys.stdin.readline
from math import*
from random import*
from decimal import*
p=[2,3,5,7,11,13,17,19,23,29,31,37,41]

def pow(x,y,p):
    if y<2:
        return (x**y)%p
    if y%2:
        return (pow(x,y//2,p)**2*x)%p
    else:
        return (pow(x,y//2,p)**2)%p

def mil(n,a):
    s,d=0,n-1
    while not d%2:
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
    if n in p:
        return True
    if n==1 or not n%2:
        return False
    for k in p:
        if not mil(n,k):
            return False
    return True

def rho(n):
    if pri(n):
        return n
    if n==1:
        return 1
    if not n%2:
        return 2
    x,c,d=randint(2,n-1),randint(1,n-1),1
    y=x
    while d==1:
        x=(x**2+c)%n
        y=(y**2+c)%n
        y=(y**2+c)%n
        d=gcd(n,abs(x-y))
        if d==n:
            return rho(n)
    if pri(d):
        return d
    return rho(d)

while True:
    n=int(input())
    if n==0:
        break
    if n==1:
        print(0)
        continue
    res=Decimal(n)
    a=[]
    while n>1:
        q=rho(n)
        a.append(q)
        n//=q
    a=list(set(a))
    for i in a:
        res*=Decimal(1)-(Decimal(1)/Decimal(i))
    print(int(res))