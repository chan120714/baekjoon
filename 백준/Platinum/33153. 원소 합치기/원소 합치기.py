n,k=map(int,input().split())
a=list(map(int,input().split()))
m=n-k

def f(x):
    cnt=0
    cur=0
    for i in a:
        cur|=i
        if cur&x==x:
            cnt+=1
            if cnt>=m:return 1
            cur=0
    return 0

res=0
for i in range(30,-1,-1):
    if f(res|(1<<i)):res|=1<<i

print(res)
