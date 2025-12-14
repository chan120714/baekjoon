from math import comb,gcd
n,m=map(int,input().split())

res=comb((n+1)*(m+1),3)
res-=(m+1)*comb(n+1,3)
res-=(n+1)*comb(m+1,3)
for i in range(1,n+1):
    for j in range(1,m+1):
        res-=2*(gcd(i,j)-1)*(n+1-i)*(m+1-j)
print(res)