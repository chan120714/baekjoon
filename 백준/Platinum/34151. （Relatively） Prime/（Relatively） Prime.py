import sys
input=sys.stdin.readline
M=998244353
o=pow
for _ in range(int(input())):
    p,n,m=map(int,input().split());
    if n<m:n,m=m,n
    x=o(p,m,M);r=n//m*(x==1)or x*(o(x,n//m,M)-1)*o(x-1,-1,M)%M
    if n%m:r+=o(p,n,M)
    print(r%M)