import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
x,y=map(int,input().split())
dijkstra(1)
n1=distance[x]
n2=distance[y]
distance=[INF]*(n+1)
dijkstra(x)
n1_1=distance[y]
n2_2=distance[n]
distance=[INF]*(n+1)
dijkstra(y)
n1_2=distance[n]
n2_1=distance[x]
if min(n1+n1_1+n1_2,n2+n2_1+n2_2)>=INF:
    print(-1)
else:
    print(min(n1+n1_1+n1_2,n2+n2_1+n2_2))