a,b,c,d=map(int,input().split())
e=0
if c*2<=d:
    print(c*(a+b))
else:
    while a+b>0:
        if a>0 and b>0:
            if a>b:
                e+=d*b
                a-=b
                b=0
            else:
                e+=d*a
                b-=a
                a=0
        elif a>0 and b==0:
            if a%2==0:
                if d>c:
                    e+=c*a
                    a=0
                elif d<=c:
                    e+=d*a
                    a=0
            else:
                if c>d:
                    e+=d*((a//2)*2)+c
                    a=0
                elif c<=d:
                    e+=c*a
                    a=0
        elif a==0 and b>0:
            if b%2==0:
                if d>=c:
                    e+=c*b
                    b=0
                elif d<c:
                    e+=d*b
                    b=0
            else:
                if c>d:
                    e+=d*((b//2)*2)+c
                    b=0
                elif c<=d:
                    e+=c*b
                    b=0
    print(e)