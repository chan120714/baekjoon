import sys
input=sys.stdin.readline
from math import *
n=int(input())
a=list(map(int,input().split()))
tree=[0]*(1<<ceil(log2(n)+1))
def init(node,start,end):
    if start==end:
        k=a[start]%2
        tree[node]=k
    else:
        init(node*2,start,(start+end)//2)
        init(node*2+1,(start+end)//2+1,end)
        tree[node]=tree[node*2]+tree[node*2+1]
def update(node,start,end,index,val):
    if index<start or index>end:
        return
    if start==end:
        a[index]=val
        tree[node]=(val%2)
        return
    update(node*2,start,(start+end)//2,index,val)
    update(node*2+1,(start+end)//2+1,end,index,val)
    tree[node]=tree[node*2]+tree[node*2+1]
def query(node,start,end,left,right):
    if right<start or left>end:
        return 0
    if left<=start and right>=end:
        return tree[node]
    lsum=query(node*2,start,(start+end)//2,left,right)
    rsum=query(node*2+1,(start+end)//2+1,end,left,right)
    return lsum+rsum
init(1,0,n-1)
for i in range(int(input())):
    q,w,e=map(int,input().split())
    if q==1:
        update(1,0,n-1,w-1,e%2)
    elif q==2:
        print((e-w+1)-query(1,0,n-1,w-1,e-1))
    else:
        print(query(1,0,n-1,w-1,e-1))