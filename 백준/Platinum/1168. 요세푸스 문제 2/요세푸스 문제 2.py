from math import *
n,m=map(int,input().split())
tree=[0]*(1<<ceil(log2(n)+1))
def init(node,start,end):
    if start==end:
        tree[node]=1
    else:
        mid=(start+end)//2
        init(node*2,start,mid)
        init(node*2+1,mid+1,end)
        tree[node]=tree[node*2]+tree[node*2+1]
init(1,0,n-1)
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
i=1
print("<",end='')
for _ in range(n):
    s=n-_
    i+=m-1
    if i%s==0:
        i=s
    elif i>s:
        i%=s
    q=query(1,0,n-1,i)
    update(1,0,n-1,q)
    if _==q-1:
        print(1+q,end='')
    else:
        print(1+q,end='')
    if n-1!=_:
        print(',',end=' ')
print(">")