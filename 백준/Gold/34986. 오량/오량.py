import math
M=10**9+7
for i in' '*int(input()):
 n=int(input());*a,=map(int,input().split());r=1
 if max(a)<2:print(1);continue
 for i in a:
  r=r*math.comb(n,i)%M;n-=i
 print(r)