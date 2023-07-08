from collections import deque
import sys
input=sys.stdin.readline
a=int(input())
graph=[list(map(int,input().rstrip())) for i in range(a)]
q=deque()
q.append((0,0))
visit=[[-1 for i in range(a)] for i in range(a)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
visit[0][0]=0
if graph[0][0]==0:
    visit[0][0]+=1
while q:
    x,y=q.popleft()
    for i in range(4):
        fx=x+dx[i]
        fy=y+dy[i]
        if 0<=fx<a and 0<=fy<a:
            if graph[fx][fy]==1 and visit[fx][fy]==-1:
                visit[fx][fy]=visit[x][y]
                q.append((fx,fy))
                continue
            elif graph[fx][fy]==1 and visit[x][y]<visit[fx][fy]:
                visit[fx][fy]=visit[x][y]
                q.append((fx,fy))
            elif visit[fx][fy]==-1 or visit[x][y]+1<visit[fx][fy]:
                visit[fx][fy]=visit[x][y]+1
                q.append((fx,fy))

print(visit[a-1][a-1])