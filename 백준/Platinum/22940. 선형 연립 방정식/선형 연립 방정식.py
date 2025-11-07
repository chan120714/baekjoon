n=int(input())
a=[list(map(float,input().split())) for i in range(n)]

for i in range(n):
    pivot=i

    for j in range(i+1,n):
        if abs(a[j][i])>abs(a[pivot][i]):
            pivot=j
    if a[pivot][i]==0:
        continue

    a[pivot],a[i]=a[i],a[pivot]
    
    for j in range(i+1,n):
        t=a[j][i]/a[i][i]
        for k in range(i,n+1):
            a[j][k]-=a[i][k]*t


res=[0 for i in range(n)]

for i in range(n-1,-1,-1):
    if a[i][i]==0:
        continue
    p=0
    for j in range(i+1,n):
       p+=res[j]*a[i][j]
    res[i]=(a[i][n]-p)/a[i][i]

for i in range(n):
    res[i]=round(res[i])
print(*res)