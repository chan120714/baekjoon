M=998244353
k=int(input())
n=1<<k
*a,=map(int,input().split())
w=n-1-sum(x>a[R:=0] for x in a[1:])
F=[1]
for i in range(n):F+=F[i]*-~i%M,
C=lambda n,k:0 if k<0 or k>n else F[n]*pow(F[k]*F[n-k],-1,M)%M
for i,x in enumerate(map(int,input().split()),1):
 s=2**i-1
 if w>=s:R=(R+x*C(w,s)*pow(C(n-1,s),-1,M))%M
print(R)