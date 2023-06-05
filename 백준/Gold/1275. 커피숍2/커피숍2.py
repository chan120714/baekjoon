import sys
input=sys.stdin.readline
from math import *
n,m=map(int,input().split())
a=list(map(int,input().split()))
tree=[0]*(1<<(ceil(log2(n)+1)))
def init(a,tree,node,st,ed):
    if st==ed:
        tree[node]=a[st]
    else:
        init(a,tree,node*2,st,(st+ed)//2)
        init(a,tree,node*2+1,(st+ed)//2+1,ed)
        tree[node]=tree[node*2]+tree[node*2+1]

def update(a,tree,node,start,end,index,val):
    if index<start or index>end:
        return
    if start==end:
        a[index]=val
        tree[node]=val
        return
    update(a,tree,node*2,start,(start+end)//2,index,val)
    update(a,tree,node*2+1,(start+end)//2+1,end,index,val)
    tree[node]=tree[node*2]+tree[node*2+1]

def query(tree,node,start,end,left,right):
    if right<start or left>end:
        return 0
    if left<=start and right>=end:
        return tree[node]
    lsum=query(tree,node*2,start,(start+end)//2,left,right)
    rsum=query(tree,node*2+1,(start+end)//2+1,end,left,right)
    return lsum+rsum

init(a,tree,1,0,n-1)

for i in range(m):
    q,w,e,r=map(int,input().split())
    if q>w:
        q,w=w,q
    print(query(tree,1,0,n-1,q-1,w-1))
    update(a,tree,1,0,n-1,e-1,r)