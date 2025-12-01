a,b=map(int,input().split())
res=abs(a-b)
n=int(input())
for i in range(n):
    k=int(input())
    res=min(res,1+abs(k-b))
print(res)
