import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[]for i in range(n+1)]
INF=1e9
distance=[INF]*(n+1)
v=int(input())
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijk(v):
    q=[]
    heapq.heappush(q,(0,v))
    distance[v]=0
    while q:
        dist,index=heapq.heappop(q)
        if distance[index]<dist:
            continue
        for i in graph[index]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijk(v)
for i in range(1,n+1):
    if distance[i]==1e9:
        print("INF")
    else:
        print(distance[i])