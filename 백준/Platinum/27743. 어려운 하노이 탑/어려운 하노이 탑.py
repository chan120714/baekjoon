a,b=map(int,input().split())
s=2
mod=10**9+7
def power(a, n):
    if n == 0:
        return 1
    
    x = power(a, n//2)%mod

    if n % 2 == 0:
        return (x * x)%mod
    
    else:
        return ((x * x)%mod * a)%mod
def r(n,m):
    if m==1:
        return power(2,n)-1
    else:
        return m*power(2,n+1)-2*m-1
print(int(r(a,b))%mod)