import sys
input=sys.stdin.readline
n,m=map(int,input().split())
from collections import deque
graph=[list(map(int,input().split())) for i in range(n)]
dist=[[i,j] for i in range(n)for j in range(m)]
res=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(n*m-2):
    for j in range(i+1,n*m-1):
        for k in range(j+1,n*m):
            if graph[dist[i][0]][dist[i][1]]!=0:
                continue
            if graph[dist[j][0]][dist[j][1]]!=0:
                continue
            if graph[dist[k][0]][dist[k][1]]!=0:
                continue
            visit=[[0 for i in range(m)]for i in range(n)]
            visit[dist[i][0]][dist[i][1]]=-1
            visit[dist[j][0]][dist[j][1]]=-1
            visit[dist[k][0]][dist[k][1]]=-1
            q=deque()
            for x in range(n):
                for y in range(m):
                    if graph[x][y]==1:
                        visit[x][y]=-1
                    elif graph[x][y]==2:
                        visit[x][y]=1
                        q.append((x,y))
            while q:
                x,y=q.popleft()
                for l in range(4):
                    fx=x+dx[l]
                    fy=y+dy[l]
                    if fx<0 or fx>=n or fy<0 or fy>=m:
                        continue
                    if visit[fx][fy]==0:
                        q.append((fx,fy))
                        visit[fx][fy]=1
            ret=0
            for x in range(n):
                for y in range(m):
                    if visit[x][y]==0:
                        ret+=1
            res=max(res,ret)
print(res)