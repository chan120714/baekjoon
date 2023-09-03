import sys
from heapq import*
input=sys.stdin.readline
a=[]
for i in range(int(input())):
    n=int(input())
    if n==0:
        if len(a)==0:
            print(0)
        else:
            print(heappop(a)[1])
    else:
        heappush(a,(abs(n),n))