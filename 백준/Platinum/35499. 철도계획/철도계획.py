import sys
input=sys.stdin.readline
sys.setrecursionlimit(9**6)
n,m=map(int,input().split())

parent=[i for i in range(123456)]

def find(x):
    if x==parent[x]:return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

g=[]
for i in range(m):
    x,y,z=map(int,input().split())
    g.append((-z,x,y))

g.sort()

res=0
for i in g:
    if find(i[1])!=find(i[2]):
        res-=i[0]
        union(i[1],i[2])
    elif find(i[1])!=find(0):
        res-=i[0]
        union(0,i[1])
print(res)
