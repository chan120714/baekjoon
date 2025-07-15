import sys
input=sys.stdin.readline
from heapq import*

k,n=map(int,input().split())

a=list(map(int,input().split()))
a.sort()
hq=[]

for i in a:
    heappush(hq,i)

res=1
while res!=n:
    k=heappop(hq)
    maxv=k
    res+=1
    for i in a:
        heappush(hq,i*k)
        if k%i==0:
            break
print(heappop(hq))

        
