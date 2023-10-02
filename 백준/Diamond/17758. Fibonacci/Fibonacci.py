import sys
from collections import*
sys.setrecursionlimit(1000000)
def pow(n,mod):
    if n==1:
        return[[1,1],[1,0]]
    if n%2==0:
        x=pow(n//2,mod)
        y=[[0,0],[0,0]]
        y[0][0]=(x[0][0]*x[0][0]+x[0][1]*x[1][0])%mod
        y[0][1]=(x[0][0]*x[0][1]+x[0][1]*x[1][1])%mod
        y[1][0]=(x[1][0]*x[0][0]+x[1][1]*x[1][0])%mod
        y[1][1]=(x[1][0]*x[0][1]+x[1][1]*x[1][1])%mod
        return y
    if n%2==1:
        x=pow(n//2,mod)
        y=[[0,0],[0,0]]
        y[0][0]=(x[0][0]*x[0][0]+x[0][1]*x[1][0])%mod
        y[0][1]=(x[0][0]*x[0][1]+x[0][1]*x[1][1])%mod
        y[1][0]=(x[1][0]*x[0][0]+x[1][1]*x[1][0])%mod
        y[1][1]=(x[1][0]*x[0][1]+x[1][1]*x[1][1])%mod
        x[0][0]=(y[0][0]+y[0][1])%mod
        x[0][1]=y[0][0]
        x[1][0]=(y[1][0]+y[1][1])%mod
        x[1][1]=y[1][0]
        return x
n=input()
ll=[-1,5,10,15,19,24,29,34,38,43,48,53,58,62,67,72,77,82,86]
k=len(n)
n=int(n)
a=3
t=deque()
if k==1:
    for i in range(1,101):
        if pow(i,10)[0][0]==n:
            print(i+1)
            exit()
    print('NIE')
    exit()
elif k==2:
    for i in range(5,10600):
        if pow(i,100)[0][0]==n:
            print(i+1)
            exit()
    print('NIE')
    exit()
elif k==3:
    for i in range(10,1550):
        if pow(i,1000)[0][0]==n:
            print(i+1)
            exit()
    print("NIE")
    exit()
elif k==4:
    for i in range(16,15500):
        if pow(i,10000)[0][0]==n:
            print(i+1)
            exit()
    print("NIE")
    exit()
for i in range(1,1501):
	if pow(i,1000)[0][0]==n%1000:
		t.append(i)
while a<=k:
	for i in range(len(t)):
		q=t.popleft()
		for j in range(10):
			if pow(q+15*(10**(a-1))*j,10**(a+1))[0][0]==n%(10**(a+1)):
				t.append(q+15*(10**(a-1))*j)
	a+=1
lll=[]
for i in t:
    lll.append(i)
lll.sort(reverse=True)
for i in lll:
	if i>=ll[k-1]+1:
		print(i+1)
		exit()
print('NIE')
