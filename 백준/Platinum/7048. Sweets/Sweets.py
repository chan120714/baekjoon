from itertools import combinations
from math import*

n,a,b=map(int,input().split())

mod = 2004

k=[int(input())for i in range(n)]


dp=[0]*(b+1)
dp[0]=1

a-=1
res1=comb(b+n,n)
res1%=2004

res2=comb(a+n,n)
res2%=2004

for i in range(1,n+1):
    for j in combinations(k,i):
        if b-i-sum(j)+n>0:
            res1+=((-1)**i)*comb(b-i-sum(j)+n,n)
            res1%=2004
        if a-i-sum(j)+n>0:
            res2+=((-1)**i)*comb(a-i-sum(j)+n,n)
            res2%=2004

print((res1-res2)%2004)