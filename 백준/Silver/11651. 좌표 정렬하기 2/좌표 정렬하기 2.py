import sys
input=sys.stdin.readline
a=[]
b=int(input())
for i in range(b):
	c,d=map(int,input().split())
	a.append([d,c])
a=sorted(a)
for j in range(b):
	print(a[j][1],a[j][0])