import sys
input=sys.stdin.readline
from bisect import *
from math import*
n=int(input())
a=[int(input()) for i in range(n)]
gr=[a[i] for i in range(n)]
gr.sort()
tree=[0]*(1<<ceil(log2(n)+1))

def update(node,start,end,index,val):
    if index>end or start>index:
        return
    if start==end:
        tree[node]=val
        return
    mid=(start+end)//2
    update(node*2,start,mid,index,val)
    update(node*2+1,mid+1,end,index,val)
    tree[node]=tree[node*2]+tree[node*2+1]

def query(node,start,end,l,r):
    if start>r or end<l:
        return 0
    if start>=l and r>=end:
        return tree[node]
    mid=(start+end)//2
    lsum=query(node*2,start,mid,l,r)
    rsum=query(node*2+1,mid+1,end,l,r)
    return lsum+rsum

for i in range(n):
    r=bisect_left(gr,a[i])
    c=query(1,0,n-1,r+1,n)
    print(c+1)
    update(1,0,n-1,r,1)