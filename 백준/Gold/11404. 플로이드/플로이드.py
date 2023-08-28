import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
INF=1e9
graph=[[INF for i in range(n+1)]for i in range(n+1)]
for i in range(m):
    x,y,z=map(int,input().split())
    graph[x][y]=min(graph[x][y],z)
for i in range(n+1):
    graph[i][i]=0
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]!=INF:
            print(graph[i][j],end=' ')
        else:
            print(0,end=' ')
    print()
