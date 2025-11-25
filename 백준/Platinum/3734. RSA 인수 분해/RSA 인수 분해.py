from math import isqrt
n,k=map(int,input().split())
for i in range(-100000,100001):
    if isqrt(i**2+4*n*k)**2==i**2+4*n*k:
        y=isqrt(i**2+4*n*k)
        if (i+y)%2:
            continue
        q=(i+y)//2
        if (y-i)%(2*k):
            continue
        p=(y-i)//(2*k)
        if 1<p<=q<n:
            print(p,'*',q)
            exit()
