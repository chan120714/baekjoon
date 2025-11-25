from math import *
def init(node,start,end):
    if start==end:
        tree[node]=1
    else:
        mid=(start+end)//2
        init(node*2,start,mid)
        init(node*2+1,mid+1,end)
        tree[node]=tree[node*2]+tree[node*2+1]
def update(node,start,end,index):
    tree[node]-=1
    if start==end:
        return
    else:
        mid=(start+end)//2
        if index<=mid:
            update(node*2,start,mid,index)
        else:
            update(node*2+1,mid+1,end,index)

def query(node,start,end,val):
    if start==end:
        return start
    mid=(start+end)//2
    if val<=tree[2*node]:
        return query(2*node,start,mid,val)
    else:
        return query(2*node+1,mid+1,end,val-tree[2*node])


tree=[0]
while 1:
    n,k,m=map(int,input().split())
    if n==0:break
    tree=[0]*(1<<ceil(log2(n)+1))
    init(1,0,n-1)
    i=m-k+1
    t=0
    for _ in range(n):
        s=n-_
        i+=k-1
        if i%s==0:
            i=s
        elif i>s:
            i%=s
        q=query(1,0,n-1,i)
        update(1,0,n-1,q)
        t=q+1
    print(t)
