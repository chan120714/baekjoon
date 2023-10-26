import sys
input=sys.stdin.readline
from heapq import*
n=int(input())
m=[]
for i in range(n):
    q,w=map(int,input().split())
    if w<q:
        q,w=w,q
    m.append([w,q])
m.sort()
q=[]
k=int(input())
res=0
for i in m:
    st=i[1]
    ed=i[0]
    if ed-st>k:
        continue
    heappush(q,st)
    while q:
        if q[0]<ed-k:
            heappop(q)
        else:
            res=max(res,len(q))
            break
print(res)