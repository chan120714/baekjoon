import sys
input=sys.stdin.readline
from math import*
from bisect import*
a=int(input())
n=list(map(int,input().split()))
k=1<<(ceil(log2(a)+1))
tree=[[] for i in range(k)]

def init(node,start,end):
    if start==end:
        tree[node].append(n[start])
    else:
        mid=(start+end)//2
        init(node*2,start,mid)
        init(node*2+1,mid+1,end)
        tree[node].extend(tree[node*2])
        tree[node].extend(tree[node*2+1])
        tree[node].sort()
init(1,0,a-1)

def query(node,start,end,l,r,t):
    if start>r or end<l:
        return 0
    if l<=start and end<=r:
        return len(tree[node])-bisect_right(tree[node],t)
    else:
        mid=(start+end)//2
        return query(node*2,start,mid,l,r,t)+query(node*2+1,mid+1,end,l,r,t)
ans=0
for _ in range(int(input())):
    i,j,k=map(int,input().split())
    i^=ans
    j^=ans
    k^=ans
    t=query(1,0,a-1,i-1,j-1,k)
    print(t)
    ans=t