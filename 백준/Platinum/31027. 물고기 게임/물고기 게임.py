import sys
input=sys.stdin.readline
for __ in range(1):
    n=int(input())
    a=[list(map(int,input().split())) for i in range(2)]

    if n==1:
        print(a[0][0],a[1][0])
        continue
    if n==2:
        print(max(a[1][0],a[0][1])+a[0][0],a[1][1]+min(a[1][0],a[0][1]))
        continue
    s=sum(a[0])+sum(a[1])
    if n%2:
        k=(n-3)//2
        u=0
        d=0
        for i in range(k+1):
            u+=a[0][i]
            d+=a[1][i]
        res=u+d
        res=max(res,min(u+a[0][k+1]+d+a[1][k+1],sum(a[0])))
        print(res,s-res)
    else:
        k=(n-2)//2
        u=0
        d=0
        for i in range(k+2):
            u+=a[0][i]
            d+=a[1][i]
        s=sum(a[0])+sum(a[1])
        res=s-(u+d)
        res=max(res,min(s-(u-a[0][k+1]+d-a[1][k+1]),sum(a[1])))
        print(s-res,res)