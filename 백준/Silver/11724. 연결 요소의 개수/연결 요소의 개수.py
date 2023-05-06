import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
n,m=map(int,input().split())
graph=[[0 for i in range(n+1)]for i in range(n+1)]
visit=[0 for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u][v],graph[v][u]=1,1
def dfs(a):
    if visit[a]==1:
        return False
    visit[a]=1
    for i in range(1,n+1):
        if visit[i]==0 and graph[a][i]==1:
            dfs(i)
    return True
res=0
for i in range(1,1+n):
    if dfs(i)==True:
        res+=1
print(res)