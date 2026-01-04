from itertools import combinations

n,m=map(int,input().split())
a=list(map(int,input().split()))
MOD=10**9+7

s=0
for i in a:
    s+=i**2

dp=[[0 for i in range(1<<20)]for i in range(21)]


dp[0][0]=1

for i in range(n):
    dp[1][1<<i]=a[i]**2*pow(s,-1,MOD)%MOD


for i in range(1,m):
    for j in combinations(range(n),i):
        t=0
        v=0
        for k in j:
            t|=1<<k
            v+=a[k]**2
        
        for k in range(n):
            if (1<<k)&t:continue
            dp[i+1][(1<<k)|t]+=dp[i][t]*(a[k]**2)*pow(s-v,-1,MOD)%MOD
            dp[i+1][(1<<k)|t]%=MOD

res=0

for i in combinations(range(n),m):
    t=0
    for k in i:
        t|=1<<k
    if t&1:
        res+=dp[m][t]
        res%=MOD
print(res)
