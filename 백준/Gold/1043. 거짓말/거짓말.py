import sys
input=sys.stdin.readline

n,m=map(int,input().split())
parent=[i for i in range(123)]

def find(x):
    if x==parent[x]:return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if (x>y): x,y=y,x
    parent[y]=x
    return

a=[]
for i in list(map(int,input().split()))[1:]:
    a.append(i)
if len(a)==0:
    print(m)
    exit()
for i in a[1:]:
    union(i,a[0])

q=[]
for i in range(m):
    t=list(map(int,input().split()))
    q.append(t[1:])
    for i in t[2:]:
        union(i,t[1])
res=0
for i in q:
    ret=1
    for j in i:
        if find(j)==find(a[0]):
            ret=0
            break
    res+=ret
print(res)
