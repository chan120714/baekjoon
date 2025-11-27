n,m=map(int,input().split())
input()
f=1
M=10**9+7
for i in range(n):f=f*-~i%M
a=input()
if a=='S':print(1)
else:print(pow((2*f*pow(n,-n,M)+n+1)*pow(4,-1,M),m,M))