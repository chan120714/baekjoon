import sys
input=sys.stdin.readline
a=int(input())
b=[]
INF=1e9
for _ in range(a):
    b.append(list(map(int,input().split())))
res=INF
for j in range(3):
    dp = [[0]*3 for _ in range(a)]
    dp[1][0],dp[1][1],dp[1][2]=b[0][j]+b[1][0],b[0][j]+b[1][1],b[0][j]+b[1][2]
    dp[1][j]=INF
    for i in range(2,a-1):
        dp[i][0]=min(dp[i-1][1]+b[i][0],dp[i-1][2]+b[i][0])
        dp[i][1]=min(dp[i-1][0]+b[i][1],dp[i-1][2]+b[i][1])
        dp[i][2]=min(dp[i-1][0]+b[i][2],dp[i-1][1]+b[i][2])
    if j==0:
        res=min(res,dp[a-2][0]+b[-1][1],dp[a-2][0]+b[-1][2],dp[a-2][1]+b[-1][2],dp[a-2][2]+b[-1][1])
    if j==1:
        res=min(res,dp[a-2][1]+b[-1][0],dp[a-2][1]+b[-1][2],dp[a-2][0]+b[-1][2],dp[a-2][2]+b[-1][0])
    if j==2:
        res=min(res,dp[a-2][2]+b[-1][1],dp[a-2][2]+b[-1][0],dp[a-2][1]+b[-1][0],dp[a-2][0]+b[-1][1])
print(res)