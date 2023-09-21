import sys
from math import*
input=sys.stdin.readline
MAX=1048576
n=int(input())
a=list(map(int,input().split()))
tree=[0]*MAX
def init(node,st,ed):
    if st==ed:
        tree[node]=a[st]
    else:
        init(node*2,st,(st+ed)//2)
        init(node*2+1,(st+ed)//2+1,ed)
        tree[node]=tree[node*2]+tree[node*2+1]

def update(node,start,end,index,value):
    if index<start or index>end:
        return
    if start==end:
        tree[node]+=value
        return
    node*=2
    mid=(start+end)//2
    update(node,start,mid,index,value)
    update(node+1,mid+1,end,index,value)
    tree[node//2]=tree[node]+tree[node+1]
    return

def query(node,start,end,l,r):
    if r<start or l>end:
        return 0
    if l<=start and end<=r:
        return tree[node]
    mid=(start+end)//2
    ls=query(node*2,start,mid,l,r)
    rs=query(node*2+1,mid+1,end,l,r)
    return ls+rs

init(1,0,n-1)

for i in range(int(input())):
    a,*q=map(int,input().split())
    if a==1:
        update(1,0,n-1,q[0]-1,q[1])
    else:
        mi,ma=0,n-1
        while mi<ma:
            mid=(mi+ma)//2
            if query(1,0,n-1,0,mid)>=q[0]:
                ma=mid
            else:
                mi=mid+1
        print((ma+mi)//2+1)