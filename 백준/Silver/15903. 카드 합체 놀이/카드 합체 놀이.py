import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
k=list(map(int,input().split()))
a=[]
for i in range(n):
    heapq.heappush(a,k.pop())
for i in range(m):
    q=heapq.heappop(a)
    w=heapq.heappop(a)
    t=q+w
    heapq.heappush(a,t)
    heapq.heappush(a,t)
print(sum(a))