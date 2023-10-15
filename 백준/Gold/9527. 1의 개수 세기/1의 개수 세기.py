def f(x):
    res=0
    a=x
    t=1
    while a>0:
        res+=(x+1)//(t*2)*t
        if a%2:
            res+=(x+1)%t
        a//=2
        t*=2
    return res
n,m=map(int,input().split())
print(f(m)-f(n-1))