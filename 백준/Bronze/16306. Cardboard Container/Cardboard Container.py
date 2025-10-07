n=int(input())
res=1e18
for i in range(1,n+1):
    if n%i:continue
    for j in range(1,n+1):
        if n%(i*j):continue
        k=n//(i*j)
        res=min(res,i*j*2+i*k*2+j*k*2)
print(res)