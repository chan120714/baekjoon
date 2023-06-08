import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
INF=1e9
distance=[INF]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
def dijkstra(v):
    q=[]
    heapq.heappush(q,(0,v))
    distance[v]=0
    while q:
        dis,node=heapq.heappop(q)
        if distance[node]<dis:
            continue
        for i in graph[node]:
            cost=i[1]+dis
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
a,b=map(int,input().split())
dijkstra(a)
print(distance[b])