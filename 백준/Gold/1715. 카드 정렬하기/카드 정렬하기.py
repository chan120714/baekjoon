import sys
input=sys.stdin.readline
from heapq import*
a=int(input())
k=[int(input())for i in range(a)]
k.sort()
t=0
for i in range(a-1):
    n,m=heappop(k),heappop(k)
    heappush(k,n+m)
    t+=n+m
print(t)