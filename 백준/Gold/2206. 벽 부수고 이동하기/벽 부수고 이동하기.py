import sys
input=sys.stdin.readline
n,m=map(int,input().split())
from collections import deque
q=deque()
graph=[list(map(int,input().rstrip()))for i in range(n)]
visit=[[[0 for i in range(m)]for i in range(n)]for i in range(2)]
q.append((0,0,0))
dx=[0,0,-1,1]
dy=[1,-1,0,0]
visit[0][0][0]=1
while q:
    x,y,t=q.popleft()
    for i in range(4):
        fx=x+dx[i]
        fy=y+dy[i]
        if fx<0 or fx>=n or fy<0 or fy>=m:
            continue
        if graph[fx][fy]==1:
            if t==1:
                continue
            visit[1][fx][fy]=visit[0][x][y]+1
            q.append((fx,fy,1))
        else:
            if t==0:
                if visit[0][fx][fy]!=0:
                    continue
                visit[0][fx][fy]=visit[0][x][y]+1
                q.append((fx,fy,0))
            else:
                if visit[1][fx][fy]!=0:
                    continue
                visit[1][fx][fy]=visit[1][x][y]+1
                q.append((fx,fy,1))
res0=visit[0][-1][-1]
res1=visit[1][-1][-1]
if res0==0 and res1==0:
    print(-1)
elif res0==0:
    print(res1)
elif res1==0:
    print(res0)
else:
    print(min(res1,res0))