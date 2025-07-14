import sys
input=sys.stdin.readline
MOD=10**9+7
fa=[1]*123412
infa=[1]*124123
for i in range(1,100213):
    fa[i]=fa[i-1]*i%MOD
infa[100001]=pow(fa[100001],-1,MOD)
for i in range(100001,0,-1):
    infa[i-1]=infa[i]*i%MOD

for __ in range(int(input())):
    a,b,d=map(int,input().split())
    y=[0]*(d+2)
    t=0
    for i in range(1,d+2):
        t+=pow(i,d,MOD)
        t%=MOD
        y[i]=t

    al=[0]*(d+2)
    for i in range(d+2):
        v=y[i]*infa[i]*infa[d+1-i]%MOD
        if (d+1-i)&1:
            v=MOD-v
        al[i]=v

    def s(n):
        if n<d+2:
            return y[n]
        p=[1]*(d+3)
        for i in range(d+2):
            p[i+1]=p[i]*(MOD+n-i)%MOD
        s=[1]*(d+3)
        for i in range(d+1,-1,-1):
            s[i]=s[i+1]*(MOD+n-i)%MOD

        res=0
        for i in range(d+2):
            k=p[i]*s[i+1]%MOD
            res+=k*al[i]
            res%=MOD
        return res%MOD

    print((s(b)-s(a-1))%MOD)