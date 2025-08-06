import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
from math import *
n=int(input())
a=[int(input())for i in range(n)]
tree=[0]*(1<<ceil(log2(n)+1))

def init(node,start,end):
	if start==end:
		tree[node]=start
	else:
		mid=(start+end)//2
		init(node*2,start,mid)
		init(node*2+1,mid+1,end)
		if a[tree[node*2]]<=a[tree[node*2+1]]:
			tree[node]=tree[node*2]
		else:
			tree[node]=tree[node*2+1]

init(1,0,n-1)

def query(node,start,end,i,j):
	if i>end or j<start:
		return -1
	if i<=start and end<=j:
		return tree[node]
	mid=(start+end)//2
	ma=query(node*2,start,mid,i,j)
	mx=query(node*2+1,mid+1,end,i,j)
	if ma==-1:
		return mx
	elif mx==-1:
		return ma
	else:
		if a[ma]<=a[mx]:
			return ma
		else:
			return mx
	
def large(start,end):
	m=query(1,0,n-1,start,end)
	ar=(end-start+1)*a[m]
	if start<=m-1:
		temp=large(start,m-1)
		if ar<temp:
			ar=temp
	if m+1<=end:
		temp=large(m+1,end)
		if ar<temp:
			ar=temp
	return ar

print(large(0,n-1))