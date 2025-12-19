M=10**9+7;i=r=1
f=[1]+[i:=i*j%M for j in range(1,7**7)]
i=map(int,open(0).read().split()[1:])
for a,b in zip(i,i):r=r*(f[a+b]*pow(f[a]*f[b],-1,M)-1)%M
print(r)