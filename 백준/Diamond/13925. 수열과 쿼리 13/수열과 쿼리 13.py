from math import*
import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
MOD=1000000007
tree=[0]*300000
temp=[0]*300000
tmp=[1]*300000

def init(node,st,ed):
    if st==ed:
        tree[node]=a[st-1]
    else:
        init(node*2,st,(st+ed)//2)
        init(node*2+1,(st+ed)//2+1,ed)
        tree[node]=(tree[node*2]+tree[node*2+1])%MOD
        
def lazy(node,st,ed):
    if temp[node]==0 and tmp[node]==1:
        return
    tree[node]=tmp[node]*tree[node]+(ed-st+1)*temp[node]
    tree[node]%=MOD
    if st!=ed:
        tmp[node*2]=tmp[node]*tmp[node*2]
        temp[node*2]=tmp[node]*temp[node*2]+temp[node]
        tmp[node*2]%=MOD
        temp[node*2]%=MOD
        tmp[node*2+1]=tmp[node]*tmp[node*2+1]
        temp[node*2+1]=tmp[node]*temp[node*2+1]+temp[node]
        tmp[node*2+1]%=MOD
        temp[node*2+1]%=MOD
    tmp[node]=1
    temp[node]=0
    
def update(node,st,ed,l,r,m,p):
    lazy(node,st,ed)
    if r<st or ed<l:
        return
    if l<=st and ed<=r:
        tmp[node]*=m
        tmp[node]%=MOD
        temp[node]*=m
        temp[node]+=p
        temp[node]%=MOD
        lazy(node,st,ed)
        return
    update(node*2,st,(st+ed)//2,l,r,m,p)
    update(node*2+1,(st+ed)//2+1,ed,l,r,m,p)
    tree[node]=(tree[node*2]+tree[node*2+1])%MOD
    
def query(node,st,ed,l,r):
    lazy(node,st,ed)
    if l>ed or r<st:
        return 0
    if l<=st and ed<=r:
        return tree[node]
    ls=query(node*2,st,(st+ed)//2,l,r)
    rs=query(node*2+1,(st+ed)//2+1,ed,l,r)
    return (ls+rs)%MOD

init(1,1,n)

m=int(input())
for i in range(m):
    t,*k=map(int,input().split())
    if t==1:
        update(1,1,n,k[0],k[1],1,k[2])
    elif t==2:
        update(1,1,n,k[0],k[1],k[2],0)
    elif t==3:
        update(1,1,n,k[0],k[1],0,k[2])
    else:
        print(query(1,1,n,k[0],k[1]))