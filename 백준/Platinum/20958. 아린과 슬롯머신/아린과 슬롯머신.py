import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
from math import *
from random import*
from collections import defaultdict
p=[2,3,5,7,11,13,17,19,23,29,31,37,41]

#분할정복 함수
def pow(x,y,p):
    if y<2:
        return (x**y)%p
    if y%2:
        return (pow(x,y//2,p)**2*x)%p
    return (pow(x,y//2,p)**2)%p

#밀러 라빈
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

def pri(n):#소수 판별
    if n in p:
        return True
    if n==1 or n%2==0:
        return False
    for k in p:
        if not mil(n,k):
            return False
    return True

def rho(n):#폴라드 로
    if pri(n):
        return n
    if n==1:
        return 1
    if n%2==0:
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

n,m=map(int,input().split())
a=list(map(int,input().split()))
if any(x%7 for x in a):
    print(-1)
    exit()

d=[0]*51203
cur=0
for i in range(n):
    a[i]//=7
    if a[i]%7<1:
        print(-1);exit()
res=0

t=defaultdict(int)
for i in range(n):
    if i>=m:
        b=a[i-m]
        while b>1:
            o=rho(b)
            while b%o<1:
                if t[o]>0:
                    t[o]-=1
                b//=o
    
    b=a[i]
    while b>1:
        o=rho(b)
        v=0
        while b%o<1:
            v+=1
            b//=o
        for j in range(min(t[o],v)):
            a[i]//=o
        if v>t[o]:
            res+=v-t[o]
            t[o]=v
print(res)
