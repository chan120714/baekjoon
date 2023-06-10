import heapq
import sys
input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for i in range(n+1)]
INF=1e9
distance=[INF]*(n+1)
graph_1=[[] for i in range(n+1)]
distance_1=[INF]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    graph[b].append((a,c))
    graph_1[a].append((b,c))
def dijkstra(v):
    q=[]
    heapq.heappush(q,(0,v))
    distance[v]=0
    while q:
        dist,node=heapq.heappop(q)
        if distance[node]<dist:
            continue
        for i in graph[node]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
def dijkstra_1(v):
    q=[]
    heapq.heappush(q,(0,v))
    distance_1[v]=0
    while q:
        dist,node=heapq.heappop(q)
        if distance_1[node]<dist:
            continue
        for i in graph_1[node]:
            cost=dist+i[1]
            if cost<distance_1[i[0]]:
                distance_1[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(v)
dijkstra_1(v)
distance_1[0]=0
distance[0]=0
for i in range(n+1):
    distance[i]+=distance_1[i]
print(max(distance))