import sys
input=sys.stdin.readline
k=1
while True:
    a=int(input())
    if a==0:
        break
    INF=1e9
    g=[[INF for i in range(a)]for i in range(a)]
    graph=[list(map(int,input().split())) for i in range(a)]
    from collections import deque
    q=deque()
    q.append((0,0))
    g[0][0]=graph[0][0]
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    while q:
        x,y=q.popleft()
        for i in range(4):
            fx=dx[i]+x
            fy=dy[i]+y
            if 0<=fx<a and 0<=fy<a:
                if g[fx][fy]==INF or g[fx][fy]>graph[fx][fy]+g[x][y]:
                    g[fx][fy]=g[x][y]+graph[fx][fy]
                    q.append((fx,fy))
    print(f"Problem {k}: {g[-1][-1]}")
    k+=1