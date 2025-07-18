from fractions import Fraction
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    if a[i][i]==0:
        continue
    for j in range(i+1,n):
        t=Fraction(a[j][i],a[i][i])
        for k in range(i,n+1):
            a[j][k]-=a[i][k]*t


res=[0 for i in range(n)]

for i in range(n-1,-1,-1):
    p=0
    for j in range(n):
       p+=res[j]*a[i][j]
    res[i]=(a[i][n]-p)//a[i][i]
print(*res)