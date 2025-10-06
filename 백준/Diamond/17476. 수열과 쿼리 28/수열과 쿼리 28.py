import sys
input=sys.stdin.readline
from math import*
tree=[[0,0,0] for i in range(1<<18)]#0-max 1-min 2-sum
tmp=[0]*(1<<18)
temp=[0]*(1<<18)
n=int(input())
m=list(map(int,input().split()))
def merge(n,m):
	return max(tree[n][0],tree[m][0]),min(tree[n][1],tree[m][1]),tree[n][2]+tree[m][2]

def init(node,st,ed):
    if st==ed:
        tree[node][0]=tree[node][1]=tree[node][2]=m[st-1]
        return
    else:
        mid=(st+ed)>>1
        init(node*2,st,mid)
        init(node*2+1,mid+1,ed)
        tree[node][0]=max(tree[node<<1][0],tree[node*2+1][0])
        tree[node][1]=min(tree[node*2+1][1],tree[node<<1][1])
        tree[node][2]=tree[node<<1][2]+tree[(node<<1)+1][2]
        return
def pus(node,st,ed):
	if tmp[node]==0 and temp[node]==0:
		return
	if temp[node]==0:
		tree[node][0]+=tmp[node]
		tree[node][1]+=tmp[node]
		tree[node][2]+=(ed-st+1)*tmp[node]
		if st^ed:
			tmp[node*2]+=tmp[node]
			tmp[node*2+1]+=tmp[node]
	else:
		tree[node][0]=tree[node][1]=tmp[node]+temp[node]
		tree[node][2]=(ed-st+1)*(tmp[node]+temp[node])		
		if st^ed:
			tmp[node*2]=tmp[node]
			tmp[node*2+1]=tmp[node]
			temp[node*2]=temp[node]
			temp[node*2+1]=temp[node]
	tmp[node]=0
	temp[node]=0
def query(node,st,ed,l,r):
	pus(node,st,ed)
	if r<st or ed<l:
		return 0
	if l<=st and ed<=r:
		return tree[node][2]
	m=(st+ed)//2
	return query(node*2,st,m,l,r)+query(node*2+1,m+1,ed,l,r)
def add(node,st,ed,l,r,v):
	pus(node,st,ed)
	if r<st or ed<l:
		return
	if l<=st and ed<=r:
		tmp[node]=v
		pus(node,st,ed)
		return
	m=(st+ed)//2
	add(node*2,st,m,l,r,v)
	add(node*2+1,m+1,ed,l,r,v)
	tree[node][0],tree[node][1],tree[node][2]=merge(node*2,node*2+1)
def seq(node,st,ed,l,r):
	pus(node,st,ed)
	if r<st or ed<l:
		return
	if l<=st and ed<=r:
		if isqrt(tree[node][1])==isqrt(tree[node][0]):
			temp[node]=isqrt(tree[node][1])
			pus(node,st,ed)
			return
		if tree[node][1]+1==tree[node][0]:
			tmp[node]=isqrt(tree[node][1])-tree[node][1]
			pus(node,st,ed)
			return
	m=(st+ed)//2 
	seq(node*2,st,m,l,r)
	seq(node*2+1,m+1,ed,l,r)
	tree[node][0],tree[node][1],tree[node][2]=merge(node*2,node*2+1)
	return
init(1,1,n)
s=int(input())
for i in range(s):
	t,*p=map(int,input().split())
	if t==1:
		add(1,1,n,p[0],p[1],p[2])
	elif t==2:
		seq(1,1,n,p[0],p[1])
	else:
		print(query(1,1,n,p[0],p[1]))