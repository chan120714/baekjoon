import math

def phi(n):
    res=n
    for i in range(2,math.isqrt(n)+2):
        if n%i==0:
            res-=(res//i)
            while (n%i==0):
                n//=i
    if n>1:
        res-=(res//n)
    return res


n,a=map(int,input().split())
if math.gcd(n,a)!=1:
    print(n-a,-1)
else:
    print(n-a,pow(a,phi(n)-1,n))
