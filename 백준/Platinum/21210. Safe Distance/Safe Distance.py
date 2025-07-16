import sys
input=sys.stdin.readline

x,y=map(int,input().split())
n=int(input())
graph=[list(map(float,input().split()))for i in range(n)]

parent=[i for i in range(n+5)]

def find(n):
    if parent[n]==n:
        return n
    else:
        parent[n]=find(parent[n])
        return parent[n]

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    if x>y:
        x,y=y,x
    parent[y]=x

st,ed=0,max(x,y)
res=0

def f(r):
    global parent
    rr=r*r
    for fx,fy in graph:
        if fx**2+fy**2<rr:
            return False
        if (x-fx)**2+(y-fy)**2<rr:
            return False
    parent=[i for i in range(n+5)]

    for i,(fx,fy) in enumerate(graph,start=1):
        if fx<r:
            union(i,n+1)
        if x-fx<r:
            union(i,n+2)
        if fy<r:
            union(i,n+3)
        if y-fy<r:
            union(i,n+4)

    t=(2*r)**2
    for i in range(1,1+n):

        for j in range(i+1,n+1):
            if (graph[i-1][0]-graph[j-1][0])**2+(graph[i-1][1]-graph[j-1][1])**2<t:
                union(i,j)
    if find(n+1)==find(n+2):
        return False
    if find(n+3)==find(n+4):
        return False
    if find(n+1)==find(n+3):
        return False
    if find(n+2)==find(n+4):
        return False
    return True

while ed-st>1e-9:
    mid=(ed+st)/2
    if f(mid):
        res=max(mid,res)
        st=mid
    else:
        ed=mid
print(st)
