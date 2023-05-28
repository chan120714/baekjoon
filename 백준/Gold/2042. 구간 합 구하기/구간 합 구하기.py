import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
arr=[0]*(n+1)
tree=[0]*(n+1)
def sm(i):
    res=0
    while i>0:
        res+=tree[i]
        i-=(i&-i)
    return res
def update(i,d):
    while i<=n:
        tree[i]+=d
        i+=(i&-i)
def s_s(n,m):
    return sm(m)-sm(n-1)
for i in range(1,1+n):
    l=int(input())
    arr[i]=l
    update(i,l)
for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update(b,c-arr[b])
        arr[b]=c
    else:
        print(s_s(b,c))