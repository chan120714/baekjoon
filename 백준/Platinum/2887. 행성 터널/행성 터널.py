import sys
input=sys.stdin.readline
from heapq import*
parent=[i for i in range(123456)]

def find(x):
    if x==parent[x]:return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if (x>y): x,y=y,x
    parent[y]=x
    return

n=int(input())
a=[[*list(map(int,input().split())),i]for i in range(1,n+1)]
a.sort()
q=[]
for i in range(1,n):
    heappush(q,(abs(a[i][0]-a[i-1][0]),a[i][3],a[i-1][3]))
a.sort(key=lambda x:x[1])
for i in range(1,n):
    heappush(q,(abs(a[i][1]-a[i-1][1]),a[i][3],a[i-1][3]))
a.sort(key=lambda x:x[2])
for i in range(1,n):
    heappush(q,(abs(a[i][2]-a[i-1][2]),a[i][3],a[i-1][3]))

res=0

while q:
    cost,x,y=heappop(q)
    if find(x)==find(y):
        continue
    union(x,y)
    res+=cost
print(res)
