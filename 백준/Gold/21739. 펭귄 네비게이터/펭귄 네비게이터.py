M=10**9+7
f=[1]
for i in range(9**5):f+=f[i]*-~i%M,
n=int(input())
print(f[2*n]*pow(f[n]*f[n]*-~n,-1,M)%M)