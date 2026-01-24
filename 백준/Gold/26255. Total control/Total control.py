import sys
input=sys.stdin.readline
from math import pi

n,S=map(int,input().split())
g=[list(map(int,input().split())) for i in range(n)]

s=0

for i in range(n):
    s+=g[i][0]*g[i-1][1]
    s-=g[i][1]*g[i-1][0]
s=abs(s)
s/=2

d=0
for i in range(n):
    d+=((g[i][0]-g[i-1][0])**2+(g[i][1]-g[i-1][1])**2)**.5

h=1e7
l=0
while h-l>1e-7:
    m=(l+h)/2
    if m*d+s+pi*m*m>S:
        h=m
    else:
        l=m
print(l)
