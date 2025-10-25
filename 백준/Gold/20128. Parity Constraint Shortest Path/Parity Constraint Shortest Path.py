import sys
input=sys.stdin.readline

from heapq import*

n,m=map(int,input().split())

g=[[]for i in range(n+1)]

for i in range(m):
    u,v,w=map(int,input().split())
    g[u].append((v,w))
    g[v].append((u,w))

INF=1e18
visited=[[INF,INF]for i in range(n+1)]

q=[]

visited[1][0]=0

for i in g[1]:
    heappush(q,(i[1],i[0]))

while q:
    w,u=heappop(q)
    if visited[u][w%2]>w:
        visited[u][w%2]=w
    else:
        continue

    for i in g[u]:
        heappush(q,(i[1]+w,i[0]))

for i in visited[1:]:
    print(i[1] if i[1]!=INF else -1,end=' ')
    print(i[0] if i[0]!=INF else -1)