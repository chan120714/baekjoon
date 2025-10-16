import sys
input=sys.stdin.readline
mod=10**9+7
f=[1]*541
g=[1]*541
for i in range(2,510):
    f[i]=f[i-1]*i%mod
    g[i]=g[i-1]*f[i-1]%mod
   
for i in ' '*int(input()):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(list(set(a)))
    if len(b)!=n:
        print(0);continue

    sign=0
    for i in range(n):
        for j in range(i+1,n):
            if b[i]==a[j]:
                a[i],a[j]=a[j],a[i]
                sign^=1

    res=1
    for i in range(n):
        for j in range(i+1,n):
            res*=(b[j]-b[i])
            res%=mod
    res*=pow(g[n],-1,mod)
    print((1 if sign==0 else -1)*res%mod)
