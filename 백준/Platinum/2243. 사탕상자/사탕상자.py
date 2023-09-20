from math import*
import sys
input=sys.stdin.readline
MAX=2097152
MA=1000000
n=int(input())
tree=[0]*MAX
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

for i in range(n):
    a,*q=map(int,input().split())
    if a==2:
        update(1,0,MA,q[0]-1,q[1])
    else:
        mi,ma=0,MA
        while mi<ma:
            mid=(mi+ma)//2
            if query(1,0,MA,0,mid)>=q[0]:
                ma=mid
            else:
                mi=mid+1
        print((ma+mi)//2+1)
        update(1,0,MA,(ma+mi)//2,-1)