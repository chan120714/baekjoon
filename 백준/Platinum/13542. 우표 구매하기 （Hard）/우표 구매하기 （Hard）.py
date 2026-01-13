n,m,k,M=map(int,input().split())

f=[1]
for i in range(2*M+1):
    f+=f[i]*-~i%M,
def c(n,m):
 a=1
 while n>0:
  k,l=n%M,m%M
  if k<l:return 0
  else:a=a*f[k]*pow(f[l]*f[k-l],-1,M)%M
  n//=M;m//=M
 return a

res=0
for i in range(n+1):
    if (k-i)%2:continue
    res+=c(n,i)*c(n+m+(k-i)//2-1,n+m-1)%M
    res%=M
print(res)
