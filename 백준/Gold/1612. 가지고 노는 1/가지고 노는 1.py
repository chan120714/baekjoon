n=int(input())
res=1
if n%2==0 or n%5==0:
    print(-1)
    exit()
v=0
while 1:
    v*=10
    v+=1
    v%=n
    if v==0:
        print(res)
        exit()
    res+=1