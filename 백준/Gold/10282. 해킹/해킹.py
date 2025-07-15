import sys
input=sys.stdin.readline
from heapq import*

INF=10**9+7

for __ in range(int(input())):
    n,d,c=map(int,input().split())
    graph=[[]for i in range(n+1)]
    visited=[INF]*(n+1)
    for i in range(d):
        a,b,s=map(int,input().split())
        graph[b].append((a,s))

    hq=[]
    visited[c]=0
    for i in graph[c]:
        heappush(hq,(i[1],i[0]))

    while hq:
        cost,x=heappop(hq)
        if cost>=visited[x]:
            continue
        visited[x]=cost
        for i in graph[x]:
            heappush(hq,(i[1]+cost,i[0]))
    res=0
    ret=0
    for i in range(1,n+1):
        if visited[i]!=INF:
            res+=1
            ret=max(ret,visited[i])
    print(res,ret)
