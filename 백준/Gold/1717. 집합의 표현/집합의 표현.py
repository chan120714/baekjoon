import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())
a=[i for i in range(n+1)]
def find(n):
    if n!=a[n]:
        a[n]=find(a[n])
        return a[n]
    else:
        return n
def uni(n,m):
    n=find(n)
    m=find(m)
    if n<m:
        a[m]=n
    else:
        a[n]=m
for i in range(m):
    q,w,e=map(int,input().split())
    if q==0:
        uni(w,e)
    else:
        if find(w)==find(e):
            print("YES")
        else:
            print("NO")