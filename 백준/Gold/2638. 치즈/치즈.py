import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(n)]
visit=[[0 for i in range(m)]for i in range(n)]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return
    if graph[x][y]==1:
        visit[x][y]+=1
        if visit[x][y]==2:
            graph[x][y]=0
        return
    if visit[x][y]>=1:
        return
    visit[x][y]=1
    if graph[x][y]==0:
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
    return
a=1
t=0
while a!=0:
    a=0
    visit=[[0 for i in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                a+=1
    if a==0:
        print(t)
        break
    t+=1
    dfs(0,0)