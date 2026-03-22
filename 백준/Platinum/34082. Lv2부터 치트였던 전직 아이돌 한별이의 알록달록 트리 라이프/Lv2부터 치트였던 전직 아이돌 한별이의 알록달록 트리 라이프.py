import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
graph=[[]for i in range(n+1)]

for i in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dp=[[0,0] for i in range(n+1)]

def dfs(x,lst):
    v0,v1=1,0
    for i in graph[x]:
        if i==lst:continue
        dfs(i,x)
        s=(sum(dp[i]))

        v0,v1=v0*s%m,(v1*s+v0*dp[i][0])%m

    dp[x]=(v0,v1)
             
dfs(1,0)
res=0
print((pow(2,n,m)-2*(dp[1][0]+dp[1][1]))%m)
