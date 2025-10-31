import sys
input=sys.stdin.readline
from itertools import*

n,k=map(int,input().split())

INF=10**9
dp=[INF]*(1<<n)

g=[list(map(int,input().split())) for i in range(n)]
dp[(1<<n)-1]=0

d=[i for i in range(n)]

for i in range(0,n):
    for j in combinations(d,i):
        ret=1<<n
        ret-=1
        for t in j:
            ret-=(1<<t)

        for t in range(n):
            if (ret&(1<<t)):
                cur=INF
                for l in range(n):
                    if (ret&(1<<l)) and l!=t:
                        cur=min(cur,g[t][l])
                dp[ret-(1<<t)]=min(dp[ret-(1<<t)],dp[ret]+cur)


res=INF
for i in combinations(d,k):
    cur=0
    for j in i:
        cur+=1<<j
    res=min(res,dp[cur])
print(res)