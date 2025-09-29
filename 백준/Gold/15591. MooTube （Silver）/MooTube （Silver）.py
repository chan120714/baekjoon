import sys
input=sys.stdin.readline
sys.setrecursionlimit(200000)
from heapq import*
n,q=map(int,input().split())

graph=[[]for i in range(n+1)]

for i in range(1,n):
    x,y,z=map(int,input().split())
    graph[x].append((z,y))
    graph[y].append((z,x))

for i in range(q):
    INF=10**18
    visited=[INF]*(n+1)
    a,b=map(int,input().split())

    def dfs(x,t,y):
        visited[x]=t
        for i in graph[x]:
            if i[1]!=y and visited[i[1]]>min(t,i[0]):
                dfs(i[1],min(t,i[0]),x)
    dfs(b,INF,-1)
    visited[b]=0

    res=0
    for i in range(1,n+1):
        if visited[i]>=a:
            res+=1
    print(res)
