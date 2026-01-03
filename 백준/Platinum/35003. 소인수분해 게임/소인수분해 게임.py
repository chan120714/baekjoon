import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
from math import *
from random import*
from collections import defaultdict
from heapq import*

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
    if n in p:
        return True
    if n==1 or n%2==0:
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
for i in range(int(input())):
    
    n=int(input())
    k=defaultdict(int)
    while n>1:
        t=rho(n)
        while n%t<1:
            k[t]+=1
            n//=t

    q=[]
    for i in k:
        heappush(q,(-k[i],i))

    turn=1
    past=0
    while 1:
        turn^=1
        if len(q)<1:
            break
        s=heappop(q)
        if s[1]^past==0:
            if len(q)<1:
                break
            tmp=heappop(q)
            heappush(q,s)
            s=tmp
        if s[0]!=-1: heappush(q,(s[0]+1,s[1]))
        past=s[1]
    print(['yyyy7089','toycartoon'][turn^1])
