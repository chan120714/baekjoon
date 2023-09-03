import sys
from collections import*
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(map(str,input().rstrip())) for i in range(n)]
visit=[[0 for i in range(m)]for i in range(n)]
q=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]=='I':
            q.append((i,j))
            visit[i][j]=1

t=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while q:
    x,y=q.popleft()
    for i in range(4):
        fx=x+dx[i]
        fy=y+dy[i]
        if 0<=fx<n and 0<=fy<m and visit[fx][fy]==0:
            visit[fx][fy]=1
            if graph[fx][fy]=='X':
                t=t
            else:
                if graph[fx][fy]=='P':
                    t+=1
                q.append((fx,fy))
print(t if t>0 else "TT")