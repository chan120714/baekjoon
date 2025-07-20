import sys
input=sys.stdin.readline
from math import*
res=0
n,m=map(int,input().split())
a=list(map(int,input().split()))
g=a[0]-1
for i in a[1:]:
  g=gcd(g,i-1)
while g&1==0: g>>=1

div=[]
for i in range(1,int(g**.5)+1,2):
    if g%i==0:
      div.append(g//i)
      if i*i==g:continue
      div.append(i)

div.sort()
for i in div:
    if i+1>m:
        break
    k=0
    while 1<<(k+1)<=(m-1)//i:k+=1
    res+=(k+1)*m-i*((1<<(k+1))-1)
print(res)