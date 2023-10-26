import sys
input=sys.stdin.readline
mod=10007
res=0
dp=[0 for i in range(2000)]
a=input().rstrip()
k=len(a)
for i in range(k):
    for j in range(i,k):
        if a[i]==a[j]:
            dp[j]+=1
            for t in range(j+1,k):
                dp[j]+=dp[t]
for i in range(k):
    res+=dp[i]%mod
print(res%mod)