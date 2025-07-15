import sys
input=sys.stdin.readline
from heapq import*

INF=10**9+7

n,m,k=map(int,input().split())

graph=[[]for i in range(n+1)]
visited=[INF]*(n+1)
res=[-1 for i in range(n+1)]
t=[1 for i in range(n+1)]

hq=[]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

visited[1]=0
t[1]=2
if k==1: res[1]=0
for i in graph[1]:
    heappush(hq,(i[1],i[0]))

while hq:
    
    cost,x=heappop(hq)
    if t[x]>k+1:
        continue
    if t[x]==k:
        res[x]=cost
    t[x]+=1

    for i in graph[x]:
        heappush(hq,(i[1]+cost,i[0]))

for i in res[1:]:
    print(i)