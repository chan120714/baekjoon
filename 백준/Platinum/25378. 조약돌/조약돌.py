n=int(input())
*a,=map(int,input().split())
d=[0]*n
for i in range(n):
 x=a[i];d[i]=max(d[i-1],d[i])
 for j in range(i+1,n):
  x=a[j]-x
  if x<0:break
  if x==0:d[j]=max(d[j],d[i-1]+1)
print(n-d[-1])