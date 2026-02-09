m=10**9+7
n,k=map(int,input().split())
if n>=k:print(~-2**k%m)
else:
    f=[1]
    for i in range(6**9):f+=f[-1]*-~i%m,
    v=[0]*-~6**9
    v[-1]=pow(f[-1],-1,m)
    for i in range(6**9-1,-1,-1):v[i]=v[i+1]*-~i%m
    s=0
    for i in range(n):s+=f[k]*v[k+~i]*v[-~i]%m
    print(s%m)