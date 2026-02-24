def f(n):
    l=1
    res=0
    while l<=n:
        r=n//(n//l)
        res+=n//l*(l+r)*(r-l+1)//2
        l=r+1
    return res

a,b=map(int,input().split())
print(f(b)-f(a-1))