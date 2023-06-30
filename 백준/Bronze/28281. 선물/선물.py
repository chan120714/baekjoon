n,m=map(int,input().split())
a=list(map(int,input().split()))
k=1e50
for i in range(n-1):
    k=min(k,(a[i]+a[i+1])*m)
print(k)