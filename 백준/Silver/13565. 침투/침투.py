from collections import deque
n,m=map(int,input().split())

a=[list(map(int,input())) for i in range(n)]
visited=[[0]*m for i in range(n)]

q=deque()


for i in range(m):
    if a[0][i]==0:
        q.append((0,i))


while q:
    x,y=q.popleft()
    if visited[x][y]:continue
    visited[x][y]=1
    for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
        fx=dx+x
        fy=dy+y
        if 0<=fx<n and 0<=fy<m:
            if a[fx][fy]==0 and visited[fx][fy]==0:
                q.append((fx,fy))
res=0
for i in range(m):
    if visited[n-1][i]==1:
        res=1

print("YNEOS"[res^1::2])