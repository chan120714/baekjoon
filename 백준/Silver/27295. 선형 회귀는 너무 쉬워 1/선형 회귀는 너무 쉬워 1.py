from math import*

n,b=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]

x=0
y=0
for i in a:
    x+=i[0]
    y+=i[1]-b

if x==0:
    print('EZPZ')
else:
    t=gcd(x,y)
    xx=x//t
    yy=y//t
    if y%x==0:
        print(y//x)
    elif x<0:
        print(f'{-yy}/{-xx}')
    else:
        print(f'{yy}/{xx}')
