import sys
input=sys.stdin.readline
sys.setrecursionlimit(400000)
t,n,d=map(int,input().split())
graph=[[[0 for i in range(n)]for i in range(n)]for i in range(t)]

for i in range(t):
    for x in range(int(input())):
        a,b,c=map(int,input().split())
        graph[i][a-1][b-1]=c
mod=10**9+7

def mul(a,b):
    res=[[0 for i in range(n)]for i in range(n)]

    for i in range(n):
        for j in range(n):
            t=0
            for k in range(n):
                t=(t+a[i][k]*b[k][j])%mod
            res[i][j]=t%mod
    return res

def pow(m,w):
    if m==0:
        k=[[0 for i in range(n)]for i in range(n)]
        for i in range(n):
            k[i][i]=1
        return k
    if m==1:
        return w
    elif m%2==0:
        x=pow(m//2,w)
        s=mul(x,x)
        return s
    else:
        x=pow(m//2,w)
        r=mul(w,mul(x,x))
        return r

res=[[0 for i in range(n)]for i in range(n)]

for i in range(n):
    res[i][i]=1

for i in range(t):
    res=mul(res,graph[i])

res=pow(d//t,res)

for i in range(d%t):
    res=mul(res,graph[i])

for i in res:
    print(*i)