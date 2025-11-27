I=input
n,m=map(int,I().split())
I()
f=1
M=10**9+7
for i in range(n):f=f*-~i%M
if I()=='S':print(pow(2*n*pow(n+1,-1,M),m,M))
else:print(pow((2*f+n+1)*pow(4,-1,M),m,M))