import sys
input=sys.stdin.readline
from heapq import*

INF=10**18+7

n,m,k=map(int,input().split())

          
visited=[INF]*(n*k+n+1)

graph=[[]for i in range(n*k+n+1)]

for i in range(m):
    x,y,t=map(int,input().split())
    for j in range(k):
        graph[x+j*n].append((y+j*n+n,0))
        graph[y+j*n].append((x+j*n+n,0))
    for j in range(k+1):
        graph[x+j*n].append((y+j*n,t))
        graph[y+j*n].append((x+j*n,t))

visited[1]=0
hq=[]
for i in graph[1]:
    heappush(hq,(i[1],i[0]))

while hq:
    cost,x=heappop(hq)
    if cost>=visited[x]:
        continue
    visited[x]=cost
    for i in graph[x]:
        if cost+i[1]<visited[i[0]]:
            heappush(hq,(cost+i[1],i[0]))
res=INF
for i in range(k+1):
    res=min(res,visited[n+i*n])
print(res)