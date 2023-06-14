import sys
input=sys.stdin.readline
from collections import *
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(n)]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                cnt+=1
                queue.append((nx,ny))
    return cnt
que=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            que.append(bfs(i,j))
print(len(que))    
if len(que)==0:
    print(0)
    exit()
print(max(que))