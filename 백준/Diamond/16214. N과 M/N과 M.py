import sys
input=sys.stdin.readline
import math

def pow(x,y,p):
    res=1
    while y>0:
        if y%2:
            res*=x
            res%=p
        x*=x
        x%=p
        y//=2
    return res
    
def phi(n):
    res=n
    for i in range(2,math.isqrt(n)+2):
        if n%i==0:
            res-=(res//i)
            while (n%i==0):
                n//=i
    if n>1:
        res-=(res//n)
    return res

a=int(input())
def sol(n,m):
    s=1
    p=[m]*50
    for i in range(1,50):
        p[i]=phi(p[i-1])
        if p[i]==1:
            s=i
            break
    arr=[0]*32
    arr[s]=1
    for i in range(s-1,0,-1):
        arr[i]=pow(n,arr[i+1],p[i])+p[i]
    arr[0]=pow(n,arr[1],m)
    return arr[0]
    
for _ in range(a):
    n,m=map(int,input().split())
    if m==1:
        print(0)
    elif n==1:
        print(1)
    elif m==2:
        print(n%2)
    else:
        print(sol(n,m))