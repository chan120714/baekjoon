from collections import defaultdict
from math import comb
import sys
n=int(input())
t=defaultdict(int)
s=['0','A','2','3','4','5','6','7','8','9','T','J','Q','K']
input=sys.stdin.read
for i in range(1):
    a=list(map(str,input().split()))
    for j in a:
        t[s.index(j)]+=1

res=0
# runs
cur=0
ret=1
for i in range(1,14):
    if t[i]>0:
        cur+=1
        ret*=t[i]
    else:
        if cur>=3: res+=ret*cur
        cur=0
        ret=1

if cur>=3:
    res+=ret*cur
#pair
for i in range(1,14):
    res+=comb(t[i],2)*2

dp=[[0 for i in range(102)]for i in range(102)]
dp[0][0]=1
x=1
for i in range(1,14):
    for j in range(t[i]):
        for k in range(16):
            dp[x][k]=dp[x-1][k]
            if k>=min(10,i):
                dp[x][k]+=dp[x-1][k-min(10,i)]
        x+=1
res+=dp[x-1][15]*2
print(res)