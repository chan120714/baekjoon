import sys
from bisect import*
input=sys.stdin.readline
a=int(input())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
l=[0]*a
for i in range(a):
    l[n[i]-1]=i
dps=[0]*a
for i in range(a):
    dps[i]=l[m[i]-1]
dp=[dps[0]]
for i in dps[1:]:
    if dp[-1]<i:
        dp.append(i)
    else:
        k=bisect_left(dp,i)
        dp[k]=i
print(len(dp))