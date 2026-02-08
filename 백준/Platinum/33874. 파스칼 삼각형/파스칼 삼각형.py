m=10**9+7
f=[1]
for i in range(7**8):f+=f[-1]*-~i%m,
n=int(input())-2
if n==2:k=4
elif n<=3:k=n+3
else:k=4-(n%2<1)*2
print((n!=0)*f[n]*pow(f[n//2]*f[n-n//2],-1,m)%m,k)