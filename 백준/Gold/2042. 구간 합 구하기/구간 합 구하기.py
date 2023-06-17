import sys
input=sys.stdin.readline
from math import *
n,m,k=map(int,input().split())
a=[int(input()) for i in range(n)]
tree=[0]*(1<<ceil(log2(n)+1))

def init(node,start,end):
    if start==end:
        tree[node]=a[start]
        return tree[node]
    else:
        mid=(start+end)//2
        tree[node]=init(node*2,start,mid)+init(node*2+1,mid+1,end)
        return tree[node]

def update(node,start,end,index,val):
    if index>end or start>index:
        return
    if start==end:
        tree[node]=val
        a[index]=val
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
init(1,0,n-1)
for i in range(m+k):
    q,b,c=map(int,input().split())
    if q==1:
        update(1,0,n-1,b-1,c)
    else:
        print(query(1,0,n-1,b-1,c-1))