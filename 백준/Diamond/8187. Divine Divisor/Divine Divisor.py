import sys
input=sys.stdin.readline
from math import*
from random import*
from collections import Counter
p=[2,3,5,7,11,13,17,19,23,29,31]
sys.setrecursionlimit(100000)
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

def rh(n,c,d):
    return (n**2+c)%d

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
        x=rh(x,c,n)
        y=rh(y,c,n)
        y=rh(y,c,n)
        d=gcd(n,abs(x-y))
        if d==n:
            return rho(n)
    if pri(d):
        return d
    return rho(d)

t=int(input())
a=list(map(int,input().split()))
m=dict()
for i in a:
    while i>1:
        k=rho(i)
        if not m.get(k):
            m[k]=0
        while i%k==0:
            m[k]+=1
            i//=k
k=0
d=0
p=m.values()
k=max(p)
cnt=Counter(p)
d=cnt[k]
print(k)
print(2**d-1)