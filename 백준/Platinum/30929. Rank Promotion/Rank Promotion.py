import sys
input=sys.stdin.readline
from heapq import*
from collections import defaultdict
 
n,c,p,q=map(int,input().split())
s=input().rstrip()
 
dp=[0]*543232
 
for i in range(1,n+1):
    if s[i-1]=='Y':
        dp[i]=dp[i-1]+q-p
    else:
        dp[i]=dp[i-1]-p
 
res=0
st=1
minv=dp[0]
 
 
for i in range(1,n+1):
    t=i-c
    if t>=st-1:
        minv=min(minv,dp[t])
    
    if i>=st+c-1:
        if dp[i]-minv>=0:
            res+=1
            st=i+1
            minv=dp[i]
print(res)