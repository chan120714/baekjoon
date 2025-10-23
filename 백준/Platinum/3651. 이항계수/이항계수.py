import sys
input=sys.stdin.readline
from math import *
MAXV=10**15
t=[0, 1000000000000000,44721361 , 181714, 12449, 2608, 950, 473, 286, 197, 148, 119, 100, 87, 78, 72, 67, 63, 61, 59, 57, 56, 55, 54,54,54,54,54,54,54]
p=len(t)-1
n=int(input())
res=set()
for i in range(1,min(n,t[2])+1):
    while t[p]==i-1:
        p-=1
    for j in range(2,p+1):
        if comb(i,j)==n:
            res.add((i,j))
            res.add((i,i-j))
res.add((n,1))
res.add((n,n-1))
res=list(res)
res.sort()
print(len(res))
for i in res:
    print(*i)
