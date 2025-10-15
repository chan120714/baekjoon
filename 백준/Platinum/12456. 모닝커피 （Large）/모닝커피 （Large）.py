import sys
input=sys.stdin.readline
from heapq import*
for w in range(1,1+int(input())):
    n,k=map(int,input().split())
    a=[list(map(int,input().split()))for i in range(n)]
    a.sort(key=lambda x:x[1])
    q=[]
    cur=0
    for i in a:
        t=max(0,min(i[0],i[1]-cur))
        i[0]-=t
        cur+=t
        heappush(q,(i[2],t))
        while i[0] and len(q) and q[0][0]<i[2]:
            x,y=heappop(q)
            if y>i[0]:
                heappush(q,(x,y-i[0]))
                heappush(q,(i[2],i[0]))
                i[0]=0
            else:
                heappush(q,(i[2],y))
                i[0]-=y
    res=0
    for i in q:
        res+=i[0]*i[1]
    print(f"Case #{w}: {res}")
