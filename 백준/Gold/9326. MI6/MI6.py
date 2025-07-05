import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
from math import *
from random import*
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

for _ in range(int(input())):
    n=int(input())
    a=dict()
    while n>1:
        k=rho(n)
        if a.get(k,-1)==-1:
            a[k]=1
        else:
            a[k]+=1
        n//=k
    t=[]
    for i in a:
        for j in range(7):
            if a[i]&(1<<j):
                t.append(i**(1<<j))
    t.sort()
    print(*t)
