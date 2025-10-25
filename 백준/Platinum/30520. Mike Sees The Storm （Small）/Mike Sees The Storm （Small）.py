MOD=10**9+7

n,k=map(int,input().split())
f=[1]*2412312
for i in range(2,2013021):
    f[i]=f[i-1]*i%MOD

res=pow(n,k,MOD)
for i in range(n):
    res+=pow(i,k,MOD)*(f[2*n]*pow(f[n-i],-1,MOD)*pow(f[n+i],-1,MOD)-f[2*n]*pow(f[n-i-1],-1,MOD)*pow(f[n+i+1],-1,MOD))
    res%=MOD
print(res)