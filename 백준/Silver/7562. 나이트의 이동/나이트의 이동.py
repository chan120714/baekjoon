import sys
input=sys.stdin.readline
from collections import deque
q=deque()
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[1,-1,2,-2,2,-2,1,-1]
for i in range(int(input())):
    q=deque()
    a=int(input())
    graph=[[0 for i in range(a)]for i in range(a)]
    n,m=map(int,input().split())
    k,l=map(int,input().split())
    q.append((n,m))
    graph[n][m]=1
    while q:
        x,y=q.popleft()
        if graph[k][l]!=0:
            break
        for j in range(8):
            fx=x+dx[j]
            fy=y+dy[j]
            if fx<0 or fx>=a or fy<0 or fy>=a:
                continue
            if graph[fx][fy]==0:
                graph[fx][fy]=graph[x][y]+1
                q.append((fx,fy))
    print(graph[k][l]-1)