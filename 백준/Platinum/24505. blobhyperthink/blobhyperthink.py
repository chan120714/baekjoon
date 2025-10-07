y=1<<17
t=[[0]*(y|1) for _ in range(11)]
def u(a,i,v):
 while i<=y:t[a][i]+=v;i+=i&-i
def q(a,r):
 k=0
 while r:k+=t[a][r];r&=r-1
 return k%(10**9+7)
input()
for a in map(int,input().split()):
 u(0,a,1)
 for i in range(1,11):u(i,a,q(i-1,a-1))
print(q(10,y))