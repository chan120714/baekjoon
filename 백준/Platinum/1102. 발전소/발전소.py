from itertools import combinations

n=int(input())
g=[list(map(int,input().split())) for i in range(n)]


a=input().rstrip()
k=0
ret=[1<<31 for i in range(1<<20)]
for i in range(n):
    if a[i]=='Y':
        k|=1<<i

ret[k]=0

a=[i for i in range(n)]
for i in range(1,n+1):

    for j in combinations(a,i):

        t=0

        for p in j:
            t|=1<<p
            
        for i in range(n):
            if t&(1<<i):
                continue
            for j in range(n):
                if t&(1<<j):
                    ret[t|(1<<i)]=min(ret[t|(1<<i)],ret[t]+g[j][i])

m=int(input())

res=1<<31

for i in range(m,n+1):
    for j in combinations(a,i):
        t=0
        for p in j:
            t|=1<<p

        res=min(res,ret[t])
print(res if res!=1<<31 else -1)