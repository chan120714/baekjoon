import sys
input=sys.stdin.readline
from math import *
n=int(input())
a=list(map(int,input().split()))
tree=[0]*(1<<(ceil(log2(n))+1))
def init(a,tree,node,start,end):
    if start==end:
        tree[node]=a[start]
    else:
        init(a,tree,node*2,start,(start+end)//2)
        init(a,tree,node*2+1,(start+end)//2+1,end)
        tree[node]=min(tree[node*2],tree[node*2+1])
def update(a,tree,node,start,end,index,d):
    if index>end or index<start:
        return
    if start==end:
        tree[node]=d
        a[index]=d
        return
    update(a,tree,node*2,start,(start+end)//2,index,d)
    update(a,tree,node*2+1,(start+end)//2+1,end,index,d)
    tree[node]=min(tree[node*2],tree[node*2+1])
def query(tree,node,start,end,left,right):
    if left>end or right<start:
        return -1
    if left<=start and end<=right:
        return tree[node]
    lsum=query(tree,node*2,start,(end+start)//2,left,right)
    rsum=query(tree,node*2+1,(start+end)//2+1,end,left,right)
    if lsum==-1:
        return rsum
    elif rsum==-1:
        return lsum
    else:
        return min(rsum,lsum)
init(a,tree,1,0,n-1)
for i in range(int(input())):
    q,w,e=map(int,input().split())
    if q==1:
        update(a,tree,1,0,n-1,w-1,e)
    else:
        print(query(tree,1,0,n-1,w-1,e-1))