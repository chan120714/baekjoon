import math
x,y,k=map(int,input().split())
b=x+y
n=(k+b-1)//b
p=x//math.gcd(x,y)
A=B=r=0
for i in range(n,n+p+1):
 m=max(k,(i-1)*b+1)
 c=(m+x-1)//x
 if not A or c*B<A*i or c*B==A*i and m<r:A,B,r=c,i,m
print(r)