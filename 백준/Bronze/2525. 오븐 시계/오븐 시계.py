a,b=map(int,input().split())
c=int(input())
s=b+c
d=s//60
e=s%60
if s<60:
    print(a,s)
elif s>=60:
    if a+d==24:
        print(0,e)
    elif a+d>24:
        print((a+d)%24,e)
    else:
        print(a+d,e)