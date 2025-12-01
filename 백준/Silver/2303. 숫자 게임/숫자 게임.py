from itertools import combinations
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]

res=0
v=0

for i in range(n):
    cur=0
    for j in combinations(a[i],3):
        cur=max(cur,sum(j)%10)
    if cur>=res:
        res=cur
        v=i+1
print(v)