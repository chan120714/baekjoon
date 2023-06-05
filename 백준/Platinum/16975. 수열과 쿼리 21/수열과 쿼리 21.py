import sys
input=sys.stdin.readline
from math import *
def init(a,tree,node,start,end):
    if start==end:
        tree[node]=a[start]
    else:
        init(a,tree,node*2,start,(start+end)//2)
        init(a,tree,node*2+1,(start+end)//2+1,end)
        tree[node]=tree[node*2]+tree[node*2+1]

def update_l(tree,lazy,node,start,end):
    if lazy[node]!=0:
        tree[node]+=(end-start+1)*lazy[node]
        if start!=end:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0

def update_r(tree,lazy,node,start,end,left,right,diff):
    update_l(tree,lazy,node,start,end)
    if left>end or right<start:
        return
    if left<=start and end<=right:
        tree[node]+=(end-start+1)*diff
        if start!=end:
            lazy[node*2]+=diff
            lazy[node*2+1]+=diff
        return
    update_r(tree,lazy,node*2,start,(start+end)//2,left,right,diff)
    update_r(tree,lazy,node*2+1,(start+end)//2+1,end,left,right,diff)
    tree[node]=tree[node*2]+tree[node*2+1]

def query(tree,lazy,node,start,end,left,right):
    update_l(tree,lazy,node,start,end)
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree[node]
    lsum=query(tree,lazy,node*2,start,(start+end)//2,left,right)
    rsum=query(tree,lazy,node*2+1,(start+end)//2+1,end,left,right)
    return lsum+rsum

n=int(input())
a=list(map(int,input().split()))
tree=[0]*(1<<(ceil(log2(n)+1)))
lazy=[0]*(1<<(ceil(log2(n)+1)))
init(a,tree,1,0,n-1)
for i in range(int(input())):
    q=list(map(int,input().split()))
    if q[0]==1:
        update_r(tree,lazy,1,0,n-1,q[1]-1,q[2]-1,q[3])
    else:
        print(query(tree,lazy,1,0,n-1,q[1]-1,q[1]-1))