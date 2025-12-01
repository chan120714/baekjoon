n=int(input())
a,pa,b,pb=map(int,input().split())
res=(0,0)
for i in range(n+1):
    if i*pa>n:break
    if res[0]*a+res[1]*b<i*a+(n-i*pa)//pb*b:
        res=(i,(n-i*pa)//pb)

print(*res)
