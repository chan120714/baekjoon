import sys
import heapq
input=sys.stdin.readline
a=int(input())
n=[]
for _ in range(a):
    b=int(input())
    if b:
        heapq.heappush(n,(b))
    else:
        if len(n)==0:
            print(0)
        else:
            print(heapq.heappop(n))
