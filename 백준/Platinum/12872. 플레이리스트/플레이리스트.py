mod=10**9+7
dp=[[0 for i in range(123)]for i in range(123)]
n,m,p=map(int,input().split())
dp[0][0]=1

for i in range(1,p+1):
    for j in range(n+1):
        if j:
            dp[i][j]+=dp[i-1][j-1]*(n-j+1)
            dp[i][j]%=mod
        if j>m:
            dp[i][j]+=dp[i-1][j]*(j-m)
            dp[i][j]%=mod
print(dp[p][n])
