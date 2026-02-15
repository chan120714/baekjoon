M=10**9+7
n,x,y=map(int,input().split())
f=[1]
for i in range(n):f+=f[-1]*-~i%M,
a=0
print(sum(f[n-k*x+k-1]*f[n-k*y+k-1]*pow(f[k-1]**2*f[n-k*x]*f[n-k*y],-1,M) for k in range(1,1+n//max(x,y)))%M)