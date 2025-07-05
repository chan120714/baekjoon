import sys
input=sys.stdin.readline
from heapq import*
n,m=map(int,input().split())
a=list(map(int,input().split()))
p=int(input())
ist=[[]for i in range(n+1)]
for i in range(p):
    d,b,t=map(int,input().split())
    a[b-1]+=t
    ist[d].append((b,t))
q=[]
for i in range(n):
    heappush(q,(a[i],i))
v=0
f=[0]*n
while m:
    x=heappop(q)
    if f[x[1]]:
        continue
    f[x[1]]=1
    v=max(x[0],v)
    m-=1
    for i in ist[x[1]+1]:
        a[i[0]-1]-=i[1]
        heappush(q,(a[i[0]-1],i[0]-1))
print(v)
