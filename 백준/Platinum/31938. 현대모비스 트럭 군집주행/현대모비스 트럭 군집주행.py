import sys
input=sys.stdin.readline
from heapq import*

n,m=map(int,input().split())
q=[]
g=[[]for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    g[a].append((c,b))
    g[b].append((c,a))


INF=10**19
visited=[(INF,INF)]*(n+1)

for i in g[1]:
    heappush(q,(i[0],i[0],i[0]*9//10,i[1]))

visited[1]=(0,0)
visited[0]=(0,0)
while q:
    dist,c1,c2,x=heappop(q)
    if visited[x]>(dist,c1):
        visited[x]=(dist,c1)
    else:
        continue
    for i in g[x]:
        heappush(q,(dist+i[0],c2+i[0],c2+i[0]*9//10,i[1]))

res=0
for i in visited:
    res+=i[1]
print(res)