a,b=map(int,input().split())
c=int(input())
d=((b+c)//60)
if a+d>=24:
    print((a+d)-24,(b+c)%60)
else:
     print(a+d,(b+c)%60)