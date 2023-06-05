import sys
input=sys.stdin.readline
from math import *
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
j=1 << ceil(log2(n)+1)
tree=[0]*j
lazy=[0]*j

def init(node,start,end):
    if start==end:
        tree[node]=a[start]
    else:
        mid=(start+end)//2
        init(node*2,start,mid)
        init(node*2+1,mid+1,end)
        tree[node]=tree[node*2]+tree[node*2+1]

def update_lazy(node,start,end):
    if lazy[node]!=0:
        tree[node]+=(end-start+1)*lazy[node]
        if start!=end:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0

def update_range(node,start,end,left,right,diff):
    update_lazy(node,start,end)
    if right<start or left>end:
        return
    if left<=start and end<=right:
        tree[node]+=(end-start+1)*diff
        if start!=end:
            lazy[node*2]+=diff
            lazy[node*2+1]+=diff
        return
    else:
        update_range(node*2,start,(start+end)//2,left,right,diff)
        update_range(node*2+1,(start+end)//2+1,end,left,right,diff)
        tree[node]=tree[node*2]+tree[node*2+1]

def query(node,start,end,left,right):
    update_lazy(node,start,end)
    if left>end or right<start:
        return 0
    elif left<=start and end<=right:
        return tree[node]
    else:
        l=query(node*2,start,(start+end)//2,left,right)
        r=query(node*2+1,(start+end)//2+1,end,left,right)
        return l+r

init(1,0,n-1)
for i in range(m+k):
    q,*w=map(int,input().split())
    if q==2:
        z,x,c=w
        update_range(1,0,n-1,z-1,x-1,c)
    else:
        z,x=w
        print(query(1,0,n-1,z-1,x-1))