import sys
input=sys.stdin.readline
from math import *
n,m=map(int,input().split())
tree=[0]*(1<<(ceil(log2(n)+1)))
lazy=[0]*(1<<(ceil(log2(n)+1)))

def update_lazy(node,start,end):
    if lazy[node]:
        tree[node]=end-start+1-tree[node]
        if start!=end:
            lazy[node*2]^=1
            lazy[node*2+1]^=1
    lazy[node]=0
def update_range(node,start,end,left,right,diff):
    update_lazy(node,start,end)
    if right<start or left>end:
        return
    if left<=start and end<=right:
        tree[node]=end-start+1-tree[node]
        if start!=end:
            lazy[node*2]^=1
            lazy[node*2+1]^=1
        return
    else:
        update_range(node*2,start,(start+end)//2,left,right,diff)
        update_range(node*2+1,(start+end)//2+1,end,left,right,diff)
        tree[node]=tree[node*2]+tree[node*2+1] 
def query(node,start,end,left,right):
    update_lazy(node,start,end)
    if right<start or end<left:
        return 0
    elif left<=start and end<=right:
        return tree[node]
    else:
        lsum=query(node*2,start,(start+end)//2,left,right)
        rsum=query(node*2+1,(start+end)//2+1,end,left,right)
        return lsum+rsum
for i in range(m):
    a,b,c=map(int,input().split())
    if a==0:
        update_range(1,0,n-1,b-1,c-1,1)
    else:
        print(query(1,0,n-1,b-1,c-1))