from math import sqrt
for i in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    n=sqrt((d-a)**2+(e-b)**2)
    if a==d and b==e:
        if c==f:
            print(-1)
        else:
            print(0)
    else:
        if n>abs(c-f) and n<abs(c+f):
            print(2)
        elif n==abs(c+f) or n==abs(c-f):
            print(1)
        elif n>abs(c+f) or n<abs(c-f):
            print(0)
        else:
            print(-1)