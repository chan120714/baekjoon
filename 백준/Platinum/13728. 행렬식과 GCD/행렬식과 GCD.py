from math import gcd
a=[0,1,1]
MOD=10**9+7
for i in range(120312):
    a.append((a[-1]+a[-2])%MOD)

n=int(input())
res=0
for i in range(2,n+2):
    res+=a[gcd(n+1,i)]
    res%=MOD
print(res)