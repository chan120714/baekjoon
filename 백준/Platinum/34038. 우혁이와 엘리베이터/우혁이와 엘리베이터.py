import sys
input=sys.stdin.readline
from heapq import*

INF=10**18+7

n,m,e,k=map(int,input().split())
t1,t2=map(int,input().split())
          
visited=[INF]*(n*k+n+1)

graph1=[[INF for i in range(n+1)]for i in range(n+1)]

for i in range(m):
    c,t,*x=map(int,input().split())
    x.sort()
    for p in range(len(x)-1):
        graph1[x[p]][x[p+1]]=min(graph1[x[p]][x[p+1]],t*(x[p+1]-x[p]))
        graph1[x[p+1]][x[p]]=min(graph1[x[p+1]][x[p]],t*(x[p+1]-x[p]))

graph=[[]for i in range(n*k+n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        for p in range(k+1):
            if graph1[i][j]==INF: break
            graph[i+p*n].append((j+p*n,graph1[i][j]))
            
for i in range(1,n):
    for j in range(k):
        graph[i+j*n].append((i+1+j*n+n,t1+t2*j))
for i in range(n,1,-1):
    for j in range(k):
        graph[i+j*n].append((i-1+j*n+n,t1+t2*j))
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
    res=min(res,visited[e+i*n])
print(res if res!=INF else -1)