import heapq
import sys
input=sys.stdin.readline
a=[]
for i in range(int(input())):
    b=int(input())
    if b==0:
        if len(a)==0:
            print(0)
        else:
            print(-heapq.heappop(a))
    else:
        heapq.heappush(a,-b)