import sys
input=sys.stdin.readline
from collections import*
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=defaultdict(int)
for i in a:
    c[i]+=1
res=defaultdict(int)
ret=0
for i in b:
    if c[i]>0:
        c[i]-=1
        res[i]+=1
        ret+=1
print(ret)

c=defaultdict(int)

for i in a:c[i]+=1
for i in res:
    for j in range(res[i]):
        print(i,end=' ')
        c[i]-=1

for i in c:
    for j in range(c[i]):
        print(i,end=' ')
print()

c=defaultdict(int)
for i in b:c[i]+=1
for i in res:
    for j in range(res[i]):
        print(i,end=' ')
        c[i]-=1

for i in c:
    for j in range(c[i]):
        print(i,end=' ')
