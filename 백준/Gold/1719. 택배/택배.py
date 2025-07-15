import sys
input=sys.stdin.readline

INF=10**9+7
n,m=map(int,input().split())
graph=[[[INF,'-'] for i in range(n+1)]for i in range(n+1)]

for i in range(m):
    x,y,t=map(int,input().split())
    graph[x][y][0]=t
    graph[y][x][0]=t
    graph[x][y][1]=y
    graph[y][x][1]=x

for i in range(1,n+1):
    graph[i][i][0]=0
    graph[i][i][1]='-'
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if graph[j][k][0]>graph[j][i][0]+graph[i][k][0]:
                graph[j][k][0]=graph[j][i][0]+graph[i][k][0]
                graph[j][k][1]=graph[j][i][1]
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:print('-',end=' ')
        else:print(graph[i][j][1],end=' ')
    print()
