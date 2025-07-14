import sys
input=sys.stdin.readline
MOD=10**9+7

n,k=map(int,input().split())
s=list(map(int,input().split()))
res=1
t=k-sum(s)
for i in range(1,n+1):
    res*=t+i
    res%=MOD
print(res)
