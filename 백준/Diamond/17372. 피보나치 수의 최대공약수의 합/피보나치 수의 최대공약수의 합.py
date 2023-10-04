import sys
from collections import*
phi=[0]*1000000
mp=dict()
mod=1000000007
def pow(n):
    if n==0:
        return [[0]]
    if n==1:
        return[[1,1],[1,0]]
    if n%2==0:
        x=pow(n//2)
        y=[[0,0],[0,0]]
        y[0][0]=(x[0][0]*x[0][0]+x[0][1]*x[1][0])%mod
        y[0][1]=(x[0][0]*x[0][1]+x[0][1]*x[1][1])%mod
        y[1][0]=(x[1][0]*x[0][0]+x[1][1]*x[1][0])%mod
        y[1][1]=(x[1][0]*x[0][1]+x[1][1]*x[1][1])%mod
        return y
    if n%2==1:
        x=pow(n//2)
        y=[[0,0],[0,0]]
        y[0][0]=(x[0][0]*x[0][0]+x[0][1]*x[1][0])%mod
        y[0][1]=(x[0][0]*x[0][1]+x[0][1]*x[1][1])%mod
        y[1][0]=(x[1][0]*x[0][0]+x[1][1]*x[1][0])%mod
        y[1][1]=(x[1][0]*x[0][1]+x[1][1]*x[1][1])%mod
        x[0][0]=(y[0][0]+y[0][1])%mod
        x[0][1]=y[0][0]
        x[1][0]=(y[1][0]+y[1][1])%mod
        x[1][1]=y[1][0]
        return x
def s(x):
    if x<1000000:
        if phi[x]!=0:
            return phi[x]
    if x in mp:
        return mp[x]
    ret=x*x
    i=2
    while i*i<=x:
        ret-=s(x//i)
        i+=1
        ret%=mod
    d=1
    while x>=i*d:
        ret-=(x//d-(x//(d+1)))*s(d)
        ret%=mod
        d+=1
    if x<1000000:
        phi[x]=ret%mod
        return phi[x]
    mp[x]=ret%mod
    return mp[x]

phi[1]=1
def fibo(x):
    if x==0:
        return 0
    if x==1:
        return 1
    return pow(x+1)[0][0]-1
n=int(input())
res=0
k=1
def fib(x,y):
    if x==0: return fibo(y)
    return (fibo(y)-fibo(x-1))%mod
while (k*k<=n):
    res+=s(n//k)*fib(k,k)%mod
    res%=mod
    k+=1
d=1
while n>=k*d:
    res+=s(d)*fib(n//(d+1)+1,n//d)%mod
    res%=mod
    d+=1
print(res%mod)