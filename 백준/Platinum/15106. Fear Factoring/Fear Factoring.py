def f(n):
 l=1
 s=0
 while l<=n:
  r=n//(n//l)
  s+=n//l*(l+r)*(r-l+1)//2
  l=r+1
 return s
a,b=map(int,input().split())
print(f(b)-f(a-1))