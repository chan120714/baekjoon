a=0
m=0
while True:
    n,l=map(int,input().split())
    a-=n;a+=l
    m=max(m,a)
    if l==0:
        print(m)
        break