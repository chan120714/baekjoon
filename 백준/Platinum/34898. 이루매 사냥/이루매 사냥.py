import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]

a.sort(key=lambda x:x[1],reverse=True)


INF=10**18

dp=[[-INF]*(m+1) for i in range(n+1)]
dp[0][0]=0


for i in a:
    for t in range(n-1,-1,-1):

        for j in range(m-i[2],-1,-1):
            if dp[t][j]==-INF:continue

            v=dp[t][j]+i[0]+(n-t-1)*i[1]
            if v>dp[t+1][j+i[2]]:
                dp[t+1][j+i[2]]=v

res=0
for i in range(n+1):
    cur=max(dp[i])
    res=max(res,cur)
print(res)
