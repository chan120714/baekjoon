import sys
input=sys.stdin.readline
from math import factorial,gcd

n=int(input())
a=[int(input()) for i in range(n)]
k=int(input())
g=[]
for i in a:
    g.append((i%k,len(str(i))))
t=[1,1]
for i in range(5200):
    t.append(t[-1]*10%k)

graph=[[0 for i in range(k)]for i in range(1<<n)]
visited=[[0 for i in range(k)]for i in range(1<<n)]

def f(x,l,m):
    if x==(1<<n)-1:
        return 1*(l==0)
    
    if visited[x][l]:
        return graph[x][l]

    visited[x][l]=1
    for i in range(n):
        if (x&(1<<i)):
            continue
        else:
            graph[x][l]+=f(x|(1<<i),(l+g[i][0]*t[m])%k,m+g[i][1])

    return graph[x][l]
x=factorial(n)
p=f(0,0,1)
if p==0:
    print('0/1')
else:
    gg=gcd(x,p)
    x//=gg
    p//=gg
    print(f'{p}/{x}')