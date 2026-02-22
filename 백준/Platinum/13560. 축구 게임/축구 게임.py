n=int(input())
a=sorted(map(int,input().split()))
s=0
for k,x in enumerate(a,1):
    s+=x
    if s<k*~-k//2:print(-1);exit()
print(1 if s==n*(n-1)//2 else -1)