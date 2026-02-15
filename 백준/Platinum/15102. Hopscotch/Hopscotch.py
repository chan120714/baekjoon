M=10**9+7
n,x,y=map(int,input().split())
f=[1]
for i in range(n):f+=f[-1]*-~i%M,
a=0
for k in range(1,min(n//x,n//y)+1):
 r=k-1;s=n-k*x;t=n-k*y
 a=(a+f[s+r]*f[t+r]*pow(f[r]*f[r]*f[s]*f[t],-1,M))%M
print(a)