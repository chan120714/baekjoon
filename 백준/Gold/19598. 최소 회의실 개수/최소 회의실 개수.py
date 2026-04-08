import sys
input=sys.stdin.readline
from heapq import*
a=int(input())
dp=[]
for i in range(a):
	n,m=map(int,input().split())
	dp.append((n,m))
dp.sort()
k=[dp[0][1]]
res=0
for i in dp[1:]:
	if k and k[0]<=i[0]:
		heappop(k)
	heappush(k,i[1])
	res=max(res,len(k))
print(res)
