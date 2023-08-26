import sys
input=sys.stdin.readline
from math import*
n=int(input())
a=list(map(int,input().split()))
p=(1<<ceil(log2(n)+1))
tree=[0]*5000000

def update(node):
    t=p+node-1
    while t:
        tree[t]+=1
        t//=2

def query(node,start,end,l,r):
    if start>r or end<l:
        return 0
    if start>=l and r>=end:
        return tree[node]
    mid=(start+end)//2
    lsum=query(node*2,start,mid,l,r)
    rsum=query(node*2+1,mid+1,end,l,r)
    return lsum+rsum

t=0
for i in a:
    c=query(1,0,p,1+i,p)
    t+=c
    update(i)
print(t)