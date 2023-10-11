import sys
input=sys.stdin.readline
n,m,t=map(int,input().split())
dp=[[[0 for i in range(n+1)]for i in range(n+1)]for i in range(n+1)]
dp[1][1][1]=1
mod=1000000007
for i in range(2,n+1):
    for j in range(1,i+1):
        for k in range(1,i+1):
            dp[i][j][k]=dp[i-1][j-1][k]+dp[i-1][j][k-1]+dp[i-1][j][k]*(i-2)
            dp[i][j][k]%=mod
print(dp[n][m][t])