p=10**9+7
n,m=map(int,input().split())
k=max(n,m+1)+1
f=[1]
for i in range(k):f+=f[i]*-~i%p,
g=m+1
t=f[g]
s=0
for a in range(max(0,n-g),n//2+1):
 s=(s+t*pow(f[a]*f[n-2*a]*f[g-n+a],-1,p))%p
print(s)