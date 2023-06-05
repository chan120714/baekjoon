import sys
input=sys.stdin.readline
from math import *
def init(a,tree,node,start,end):
    if start==end:
        if a[start]>0:
            tree[node]=1
        elif a[start]==0:
            tree[node]=0
        else:
            tree[node]=-1
    else:
        init(a,tree,node*2,start,(start+end)//2)
        init(a,tree,node*2+1,(start+end)//2+1,end)
        if tree[node*2]*tree[node*2+1]>0:
            tree[node]=1
        elif tree[node*2]*tree[node*2+1]==0:
            tree[node]=0
        else:
            tree[node]=-1

def update(a,tree,node,start,end,index,val):
    if index<start or index>end:
        return
    if start==end:
        a[index]=val
        if a[index]>0:
            tree[node]=1
        elif a[index]==0:
            tree[node]=0
        else:
            tree[node]=-1
        return
    update(a,tree,node*2,start,(start+end)//2,index,val)
    update(a,tree,node*2+1,(start+end)//2+1,end,index,val)
    if tree[node*2]*tree[node*2+1]>0:
        tree[node]=1
    elif tree[node*2]*tree[node*2+1]==0:
        tree[node]=0
    else:
        tree[node]=-1

def query(tree,node,start,end,left,right):
    if right<start or left>end:
        return 1
    if left<=start and right>=end:
        return tree[node]
    lsum=query(tree,node*2,start,(start+end)//2,left,right)
    rsum=query(tree,node*2+1,(start+end)//2+1,end,left,right)
    return lsum*rsum
while True:
    try:
        n,m=map(int,input().split())
        a=list(map(int,input().split()))
        tree=[0]*(1 << ceil(log2(n)+1))
        init(a,tree,1,0,n-1)
        for i in range(m):
            q,w,e=map(str,input().split())
            w,e=int(w),int(e)
            if q=="C":
                update(a,tree,1,0,n-1,w-1,e)
            else:
                k=query(tree,1,0,n-1,w-1,e-1)
                if k>0:
                    print("+",end='')
                elif k==0:
                    print("0",end='')
                else:
                    print("-",end='')
        print()
    except Exception:
        break