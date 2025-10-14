def pisano(x):
    a,b=0,1
    t=1
    for i in range(x**2):
        a,b=b,(a+b)%x
        if a==0 and b==1:return t
        t+=1

for i in range(int(input())):
    n,m=map(int,input().split())
    print(n,pisano(m))
