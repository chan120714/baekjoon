import sys
input=sys.stdin.readline
def square(n):
	x=[[6,-4],[1,0]]
	t=[[0,0],[0,0]]
	p=[[0,0],[0,0]]
	if n==1:
		return x
	z=square(n//2)
	for i in range(2):
		for j in range(2):
			for k in range(2):
				t[i][j]+=z[i][k]*z[k][j]
			if j:
				t[i][j]%=-1000
			else:
				t[i][j]%=1000
	if n%2:
		for i in range(2):
			for j in range(2):
				for k in range(2):
					p[i][j]+=x[i][k]*t[k][j]
				if j:
					p[i][j]%=-1000
				else:
					p[i][j]%=1000
		return p
	else:
		return t
a=int(input())
for i in range(a):
	n=int(input())
	k=square(n)
	print('Case #%d: %.3d'%(i+1,(k[0][0]+k[1][1]-1)%1000))