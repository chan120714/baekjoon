import sys
input=sys.stdin.readline
from heapq import*

n,m=map(int,input().split())

visited=[0]*123412
graph=[[]for i in range(n+1)]


for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

a,b=map(int,input().split())
hq=[]

for i in graph[a]:
    heappush(hq,(-i[1],i[0]))
visited[a]=10**9+7
while hq:
    cost,x=heappop(hq)
    cost*=-1
    if visited[x]>=cost:
        continue
    visited[x]=cost
    for i in graph[x]:
        heappush(hq,(-min(i[1],cost),i[0]))

print(visited[b])
