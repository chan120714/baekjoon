n,m=map(int,input().split())
M=998244353
f=[1]
for i in range(7**7):f+=f[i]*-~i%M,
def C(n,r):return 0 if r<0 or r>n else f[n]*pow(f[r]*f[n-r],-1,M)%M
r=0
for i in range(max(0,-m),1+min(-~n//2,n//2-m)):r=(r+C(-~n//2,i)*C(n//2,i+m))%M
print(r)