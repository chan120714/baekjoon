import sys
input=sys.stdin.readline
from math import *
mod=1000000007
n,m,k=map(int,input().split())
a=[int(input()) for i in range(n)]
tree=[1]*(1<<(ceil(log2(n))+1))

def init(a,tree,node,start,end):
    if start==end:
        tree[node]=a[start]
    else:
        init(a,tree,node*2,start,(start+end)//2)
        init(a,tree,node*2+1,(start+end)//2+1,end)
        tree[node]=tree[node*2]*tree[node*2+1]%mod

def update(a,tree,node,start,end,index,val):
    if index<start or index>end:
        return
    if start==end:
        a[index]=val
        tree[node]=val
        return
    update(a,tree,node*2,start,(start+end)//2,index,val)
    update(a,tree,node*2+1,(start+end)//2+1,end,index,val)
    tree[node]=tree[node*2]*tree[node*2+1]%mod

def query(tree,node,start,end,left,right):
    if right<start or left>end:
        return 1
    if left<=start and right>=end:
        return tree[node]
    lsum=query(tree,node*2,start,(start+end)//2,left,right)
    rsum=query(tree,node*2+1,(start+end)//2+1,end,left,right)
    return lsum*rsum%mod

init(a,tree,1,0,n-1)

for i in range(m+k):
    q,w,e=map(int,input().split())
    if q==1:
        update(a,tree,1,0,n-1,w-1,e)
    else:
        print(query(tree,1,0,n-1,w-1,e-1)%1000000007)