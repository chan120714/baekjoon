import sys
input=sys.stdin.readline
from math import *
n,m=map(int,input().split())
a=[int(input()) for i in range(n)]
tree_min=[0]*(1<<(ceil(log2(n))+1))
tree_max=[0]*(1<<(ceil(log2(n))+1))
def init_min(a,tree,node,start,end):
    if start==end:
        tree[node]=a[start]
    else:
        init_min(a,tree,node*2,start,(start+end)//2)
        init_min(a,tree,node*2+1,(start+end)//2+1,end)
        tree[node]=min(tree[node*2],tree[node*2+1])

def init_max(a,tree,node,start,end):
    if start==end:
        tree[node]=a[start]
    else:
        init_max(a,tree,node*2,start,(start+end)//2)
        init_max(a,tree,node*2+1,(start+end)//2+1,end)
        tree[node]=max(tree[node*2],tree[node*2+1])

def query_min(tree,node,start,end,l,r):
    if l>end or r<start:
        return -1
    if l<=start and r>=end:
        return tree[node]
    lmin=query_min(tree,node*2,start,(start+end)//2,l,r)
    rmin=query_min(tree,node*2+1,(start+end)//2+1,end,l,r)
    if lmin==-1:
        return rmin
    elif rmin==-1:
        return lmin
    else:
        return min(rmin,lmin)
    
def query_max(tree,node,start,end,l,r):
    if l>end or r<start:
        return -1
    if l<=start and r>=end:
        return tree[node]
    lmax=query_max(tree,node*2,start,(start+end)//2,l,r)
    rmax=query_max(tree,node*2+1,(start+end)//2+1,end,l,r)
    if lmax==-1:
        return rmax
    elif rmax==-1:
        return lmax
    else:
        return max(rmax,lmax)
init_min(a,tree_min,1,0,n-1)
init_max(a,tree_max,1,0,n-1)
for i in range(m):
    c,d=map(int,input().split())
    print(query_min(tree_min,1,0,n-1,c-1,d-1),query_max(tree_max,1,0,n-1,c-1,d-1))