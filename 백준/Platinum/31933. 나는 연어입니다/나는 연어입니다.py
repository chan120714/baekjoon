from heapq import *
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
g=[]

for i in range(m):
    u,v,l,r=map(int,input().split())
    heappush(g,(l,r,u,v))
use=[]


k=int(input())
*a,=map(int,input().split())
a.sort()

res=0
cur=-1
ret=0
def bfs():
    parent=[i for i in range(5465)]
    def find(x):
        if parent[x]==x:return x
        parent[x]=find(parent[x])
        return parent[x]

    def union(x,y):
        x=find(x)
        y=find(y)
        if x<y:
            parent[y]=x
        else:
            parent[x]=y
    for i in use:
        union(i[1],i[2])
    if find(1)==find(n):
        return 1
    return 0
for i in a:
    while len(use) and use[0][0]<i:
        heappop(use)
        cur=-1
    while len(g) and g[0][0]<=i:
        l,r,u,v=heappop(g)
        heappush(use,(r,u,v))
        cur=-1
    if cur==-1:
        ret=bfs()
        res+=ret
        cur=1
    elif cur==1:
        res+=ret
print(res)