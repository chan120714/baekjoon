from collections import deque
import sys
input=sys.stdin.readline
while True:
    n,m,k=map(int,input().split())
    if n+m+k==0:
        break
    graph=[]
    g=[[0 for i in range(k)]for i in range(n*m)]
    for i in range((n*(m+1))):
        if i%(m+1)==m:
            input()
            continue
        graph.append(list(map(str,input())))
    dx=[-1,1,0,0,m,-m]
    dy=[0,0,-1,1,0,0]
    queue=deque()
    for i in range(n*m):
        for j in range(k):
            if graph[i][j]=='E':
                q,w=i,j
            if graph[i][j]=='S':
                queue.append((i,j))
    while queue:
            (x,y)=queue.popleft()
            for i in range(6):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=n*m or ny<0 or ny>=k:
                    continue
                if g[nx][ny]!=0:
                    continue
                if g[nx][ny]==0:
                    if graph[nx][ny]=='#':
                        continue
                    if (x%m==n-1 and nx%m==0) or (x%m==0 and nx%m==m-1):
                        continue
                    g[nx][ny]=g[x][y]+1
                    queue.append((nx,ny))
    print(f"Escaped in {g[q][w]} minute(s)." if g[q][w]!=0 else "Trapped!")