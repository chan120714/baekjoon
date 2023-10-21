import sys
input=sys.stdin.readline
mod=1000000007

def pow(x,y):
    if y<2:
        return x**y%mod
    res=pow(x,y//2)
    if y%2:
        return (res**2)*x%mod
    else:
        return (res**2)%mod
n=int(input())
m=list(map(int,input().split()))
m.sort()
res=0
for i in range(n):
    maxv=pow(2,i)
    minv=pow(2,n-i-1)
    res+=((maxv-minv)*m[i])%mod
print(res%mod)