import sys
input=sys.stdin.readline
from heapq import*
from collections import defaultdict
 
n,m,k=map(int,input().split())
 
graph=[[] for i in range(n+1)]
 
for a in range(m):
    i,j,l=map(int,input().split())
    graph[i].append((j,l))
    graph[j].append((i,l))
 
def dijk(x):
    visited=[10**18 for i in range(234567)]
    visited[x]=0
    
    q=[]
    
    for i in graph[x]:
        heappush(q,(i[1],i[0]))
    
    while q:
        cost,v=heappop(q)
        if cost>=visited[v]: continue
        visited[v]=cost
 
        for i in graph[v]:
            heappush(q,(i[1]+cost,i[0]))
    return visited
 
 
d1=dijk(1)
dn=dijk(n)
 
ret=[]
res=0
p=1
 
store=[]
for i in range(k):
    n,k=map(float,input().split())
    n=int(n)
    store.append((k,n))
 
for i in store:
    if abs(i[0]-1)<=1e-6:
        break
else:
    print('impossible')
    exit()
 
temp=defaultdict(lambda : 1)
 
for i in store:
    temp[d1[i[1]]+dn[i[1]]]*=(1-i[0])
 
 
for i in temp:
    ret.append((i,temp[i]))
 
ret.sort()
 
 
for i in ret:
    res+=i[0]*p*(1-i[1])
    p*=i[1]
print(res)