import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[list(map(int,input().split()))for i in range(m)]
INF=10**18
dp=[[INF]*(n+1)for i in range(m+1)]

dp[0][0]=0

a.sort()

for i in range(1,m+1):
    for j in range(i,0,-1):
        t=-1
        for k in range(n+1):
            if dp[j-1][k]<INF:
                t=k
                

        if t==-1:continue

        for k in range(min(n,t+a[i-1][1]),0,-1):
            dp[j][k]=min(dp[j][k],dp[j-1][min(t,k-1)]+a[i-1][0]*(k-min(t,k-1)))
        
res=INF

for i in range(1,m+1):
    res=min(res,dp[i][n]*i)

print(res)