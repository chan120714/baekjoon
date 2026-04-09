M=10**9+7
n=int(input())
a,b=sorted(map(int,input().split()))
v=[1]*-~n
for i in range(2,n+1):v[i]=M-M//i*v[M%i]%M
def C(n,r):
    if r<0 or r>n:return 0
    r=min(r,n-r);x=1
    for i in range(1,r+1):x=x*(n-r+i)%M*v[i]%M
    return x
def F(p,q):
    if not p:return pow(2,q,M)
    x=1
    for i in range(1,q+1):x=x*(p+i-1)%M*v[i]%M
    s=x
    for i in range(q,0,-1):x=x*2*i%M*v[p+i-1]%M;s=(s+x)%M
    return s
print((C(a+n-b-2,a-2)*pow(2,b-a-1,M)if b-a>1 else F(a-2,n-b)+F(n-b,a-2))%M)