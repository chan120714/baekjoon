from math import *
import sys
input=sys.stdin.readline
from random import*
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

for i in range(int(input())):
    n=int(input())
    if n==4:
        print(1)
        continue
    a=[]
    while n!=1:
        x=rho(n)
        n//=x
        a.append(x)
    if len(a)!=len(list(set(a))):
        print(-1)
    else:
        print(factorial(len(a)))