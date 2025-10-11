p=10**9+7
n,m,k=map(int,input().split())
a=[list(map(int,input().split()))for _ in' '*k]
a.sort()
a+=[(n,m)]
L=n+m
f=[1]*(L+1)
for i in range(L):f[i+1]=f[i]*(i+1)%p
g=[1]*(L+1);g[L]=pow(f[L],-1,p)
for i in range(L,0,-1):g[i-1]=g[i]*i%p
C=lambda N,R:f[N]*g[R]%p*g[N-R]%p
d=[]
for i,(x,y) in enumerate(a):
 w=C(x+y,x)
 for j,(X,Y) in enumerate(a[:i]):
  if X<=x and Y<=y:w-=d[j]*C(x-X+y-Y,x-X)
 d+=[w%p]
print(d[-1])
