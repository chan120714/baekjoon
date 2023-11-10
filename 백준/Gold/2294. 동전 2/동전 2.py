import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
INF=1e9
dp=[1e9]*(m+1)
dp[0]=0
gr=[int(input()) for i in range(n)]
q=deque()
q.append(0)
while q:
    x=q.popleft()
    for i in range(n):
        fx=gr[i]+x
        if fx>m:
            continue
        else:
            if dp[fx]>dp[x]+1:
                dp[fx]=dp[x]+1
                q.append(fx)
print(dp[m] if dp[m]!=INF else -1)