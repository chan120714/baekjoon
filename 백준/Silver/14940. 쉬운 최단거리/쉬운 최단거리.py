import sys
from collections import deque
input=sys.stdin.readline
q=deque()
a,b=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(a)]
for i in range(a):
    for j in range(b):
        if graph[i][j]==2:
            q.append((i,j))
            n,m=i,j
            graph[i][j]=2
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while q:
    x,y=q.popleft()
    for i in range(4):
            sx=x+dx[i]
            sy=y+dy[i]
            if 0<=sx<a and 0<=sy<b and graph[sx][sy]==1:
                graph[sx][sy]=graph[x][y]+1
                q.append((sx,sy))
for i in range(a):
    for j in range(b):
        if graph[i][j]==0:
            print(0,end=' ')
        else:
            print(graph[i][j]-2,end=' ')
    print()
