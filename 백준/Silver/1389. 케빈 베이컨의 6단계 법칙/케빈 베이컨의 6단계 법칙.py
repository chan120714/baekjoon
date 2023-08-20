import sys
input=sys.stdin.readline
n,m=map(int,input().split())
INF=1e9
graph=[[INF for i in range(n+1)]for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])
for i in range(1,n+1):
    graph[i][i]=0
    graph[i][0]=0
k=1
su=sum(graph[1])
for i in range(2,n+1):
    if su>sum(graph[i]):
        su=sum(graph[i])
        k=i
print(k)