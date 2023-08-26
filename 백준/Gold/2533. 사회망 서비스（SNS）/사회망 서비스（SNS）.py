import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
n=int(input())
graph=[[]for i in range(n+1)]
visit=[0 for i in range(n+1)]
dp=[[0,0] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    visit[n]=1
    dp[n][0]=1
    dp[n][1]=0
    for i in graph[n]:
        if visit[i]==0:
            dfs(i)
            dp[n][0]+=dp[i][1]
            dp[n][1]+=max(dp[i][0],dp[i][1])
dfs(1)
print(n-max(dp[1][0],dp[1][1]))