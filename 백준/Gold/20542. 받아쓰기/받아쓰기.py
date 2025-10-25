n,m=map(int,input().split())
a=input()
b=input()

dp=[[0 for i in range(m+1)]for i in range(n+1)]

for i in range(m+1):dp[0][i]=i
for i in range(n+1):dp[i][0]=i
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1] or (a[i-1]=='i' and b[j-1]in'ijl') or (a[i-1]=='v' and b[j-1]=='w'):
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
print(dp[n][m])
