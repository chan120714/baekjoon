import sys
input=sys.stdin.readline
from math import *
n=int(input())
a=list(map(int,input().split()))
tree=[1]*(1<<ceil(log2(n)+1))
INF=10e9
def init(node,start,end):
    if start==end:
        tree[node]=a[start]	
    else:
        init(node*2,start,(start+end)//2)
        init(node*2+1,(start+end)//2+1,end)
        tree[node]=min(tree[node*2],tree[node*2+1])

def update(node,start,end,index,val):
    if index<start or index>end:
        return
    if start==end:
        a[index]=val
        tree[node]=val
    else:
        update(node*2,start,(start+end)//2,index,val)
        update(node*2+1,(start+end)//2+1,end,index,val)
        tree[node]=min(tree[node*2],tree[node*2+1])

def query(node,start,end,left,right):
    if left>end or right<start:
        return INF
    elif left<=start and end<=right:
        return tree[node]
    else:
        l=query(node*2,start,(start+end)//2,left,right)
        r=query(node*2+1,(start+end)//2+1,end,left,right)
        if l<=r:
            return l
        else:
            return r

def find(node,start,end):
    if start==end:
        return start
    if tree[node*2]<=tree[node*2+1]:
        return find(node*2,start,(start+end)//2)
    else:
        return find(node*2+1,(start+end)//2+1,end)
def query_min(tree,node,start,end,l,r):
    if l>end or r<start:
        return (-1,-1)
    if start==end:
        return tree[node],start
    elif l<=start and r>=end:
        return tree[node],find(node,start,end)
    lmin,x=query_min(tree,node*2,start,(start+end)//2,l,r)
    rmin,y=query_min(tree,node*2+1,(start+end)//2+1,end,l,r)
    if lmin==-1:
        return (rmin,y)
    elif rmin==-1:
        return (lmin,x)
    else:
        if lmin==rmin:
            return (lmin,x)
        elif lmin<rmin:
            return (lmin,x)
        else:
            return (rmin,y)
        
init(1,0,n-1)
for i in range(int(input())):
    q=list(map(int,input().split()))
    if q[0]==1:
        update(1,0,n-1,q[1]-1,q[2])
    else:
        print(query_min(tree,1,0,n-1,0,n-1)[1]+1)