import sys
input=sys.stdin.readline
MOD=10**9+7
f=[1]*123123
for i in range(2,102121):
    f[i]=f[i-1]*i
    f[i]%=MOD
for __ in range(int(input())):
    n=input().rstrip()
    t=0
    h=0
    for i in n:
        if i=='H':
            h+=1
        if i=='?':
            t+=1
    res=0
    for i in range(1+t):
        if (i+h)%2==0:
            continue
        res+=f[t]*pow(f[i],-1,MOD)*pow(f[t-i],-1,MOD)%MOD
        res%=MOD
    print(res)
