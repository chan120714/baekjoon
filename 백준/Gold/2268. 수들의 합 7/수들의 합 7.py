import sys
input=sys.stdin.readline
from math import *
n,m=map(int,input().split())
a=[0]*n
tree=[0]*(1<<ceil(log2(n)+1))

def update(node,start,end,index,d):
    if index>end or index<start:
        return
    if start==end:
        tree[node]=d
        a[index]=d
        return
    update(node*2,start,(start+end)//2,index,d)
    update(node*2+1,(start+end)//2+1,end,index,d)
    tree[node]=tree[node*2]+tree[node*2+1]

def query(node,start,end,left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree[node]
    l=query(node*2,start,(end+start)//2,left,right)
    r=query(node*2+1,(start+end)//2+1,end,left,right)
    return l+r

for i in range(m):
    q,w,e=map(int,input().split())
    if q==0:
        if w>e:
            w,e=e,w
        print(query(1,0,n-1,w-1,e-1))
    else:
        update(1,0,n-1,w-1,e)