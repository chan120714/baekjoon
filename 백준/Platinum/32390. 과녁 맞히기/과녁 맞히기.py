n,k=map(int,input().split())
M=10**9+7
f=[1]
for i in range(7**8):f+=f[i]*-~i%M,
r=f[n]
*a,=map(int,input().split())
for i in a:r=r*pow(f[i],-1,M)*pow(2,i-1,M)%M
print(r)