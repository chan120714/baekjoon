import sys
input=sys.stdin.readline
from heapq import*
from collections import deque
INF=10**9+7
visited=[INF]*545
while 1:
    n,m=map(int,input().split())
    if n+m==0:
        break
    s,d=map(int,input().split())
    for i in range(545):
        visited[i]=INF
    graph=[[]for i in range(n+1)]
    graph1=[[]for i in range(n+1)]
    visited[s]=0

    ist=[0]*(m+1)
    
    q=[]
    for i in range(m):
        u,v,p=map(int,input().split())
        graph[u].append((v,p,i))
        graph1[v].append((u,p,i))

    for i in graph[s]:
        heappush(q,(i[1],i[0]))

    while q:
        cost,x=heappop(q)
        if cost>=visited[x]:
            continue
        visited[x]=cost
        for i in graph[x]:
            if cost+i[1]>=visited[i[0]]:
                continue
            heappush(q,(i[1]+cost,i[0]))


    q=deque()
    q.append(d)
    t=[0]*(n+1)
    while q:
        x=q.popleft()
        if t[x]:
            continue
        t[x]=1
        for i in graph1[x]:
            if visited[x]-visited[i[0]]==i[1]:
                q.append(i[0])
                ist[i[2]]=1

    q=[]
    for i in range(545):
        visited[i]=INF
    visited[s]=0

    for i in graph[s]:
        if ist[i[2]]:
            continue
        heappush(q,(i[1],i[0]))
    while q:
        cost,x=heappop(q)
        if cost>=visited[x]:
            continue
        visited[x]=cost
        for i in graph[x]:
            if cost+i[1]>=visited[i[0]]:
                continue
            if ist[i[2]]:
                continue
            heappush(q,(i[1]+cost,i[0]))
            
    print(visited[d] if visited[d]!=INF else -1)
