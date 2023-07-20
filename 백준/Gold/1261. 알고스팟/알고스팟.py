from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(map(int,input().rstrip())) for i in range(m)]
q=deque()
q.append((0,0))
visit=[[-1 for i in range(n)] for i in range(m)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
visit[0][0]=0
while q:
    x,y=q.popleft()
    for i in range(4):
        fx=x+dx[i]
        fy=y+dy[i]
        if 0<=fx<m and 0<=fy<n:
            if graph[fx][fy]==0 and visit[fx][fy]==-1:
                visit[fx][fy]=visit[x][y]
                q.append((fx,fy))
                continue
            elif graph[fx][fy]==0 and visit[x][y]<visit[fx][fy]:
                visit[fx][fy]=visit[x][y]
                q.append((fx,fy))
            elif visit[fx][fy]==-1 or visit[x][y]+1<visit[fx][fy]:
                visit[fx][fy]=visit[x][y]+1
                q.append((fx,fy))

print(visit[m-1][n-1])