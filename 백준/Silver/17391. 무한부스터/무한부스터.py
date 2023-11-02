import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(n)]
visit=[[0 for i in range(m)]for i in range(n)]
q=deque()
q.append((0,0))
visit[0][0]=1
while q:
    x,y=q.popleft()
    for i in range(1,graph[x][y]+1):
        if x+i<n:
            if visit[x+i][y]==0:
                visit[x+i][y]=visit[x][y]+1
                q.append((x+i,y))
        if y+i<m:
            if visit[x][y+i]==0:
                visit[x][y+i]=visit[x][y]+1
                q.append((x,y+i))
print(visit[-1][-1]-1)