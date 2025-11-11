import sys
input=sys.stdin.readline
from math import gcd
for _ in range(int(input())):
 q,w,e,r,t,y=map(int,input().split())
 x=r;m=q
 for y,n in((t,w),(y,e)):
  g=gcd(m,n);d=y-x
  if d%g:print(-1);break
  t=n//g
  x=(x+m*(pow(m//g,-1,t)*(d//g)%t))%(m*t);m*=t
 else:print(x)