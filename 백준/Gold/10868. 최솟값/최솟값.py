import sys
input=sys.stdin.readline
from math import *
n,m=map(int,input().split())
a=[int(input()) for i in range(n)]
tree=[0]*(1 << ceil(log2(n)+1))
INF=10e9
def init(node,start,end):
    if start==end:
        tree[node]=a[start]
    else:
        mid=(start+end)//2
        init(node*2,start,mid)
        init(node*2+1,mid+1,end)
        tree[node]=min(tree[node*2],tree[node*2+1])

def query(node,start,end,left,right):
    if left>end or right<start:
        return 10e9
    elif left<=start and end<=right:
        return tree[node]
    else:
        mid=(start+end)//2
        l=query(node*2,start,mid,left,right)
        r=query(node*2+1,mid+1,end,left,right)
        return min(l,r)

init(1,0,n-1)
for i in range(m):
    q,w=map(int,input().split())
    print(query(1,0,n-1,q-1,w-1))