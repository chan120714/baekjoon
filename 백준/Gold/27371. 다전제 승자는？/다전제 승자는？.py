mod=10**9+7
def ipow(n,k):
    res=1
    while k:
        if k&1:
            res*=n
            res%=mod
        n*=n
        n%=mod
        k>>=1
    return res
fa=[1]*523091
for i in range(2,500001):
    fa[i]=fa[i-1]*i
    fa[i]%=mod
for __ in range(int(input())):
    n,m=map(int,input().split())
    res=0
    for i in range(n):
        res+=fa[n+i-1]*fa[2*m-i-n-1]*ipow(fa[i],mod-2)*ipow(fa[n-1],mod-2)*ipow(fa[m-i],mod-2)*ipow(fa[m-n-1],mod-2)
        res%=mod
    print(res)