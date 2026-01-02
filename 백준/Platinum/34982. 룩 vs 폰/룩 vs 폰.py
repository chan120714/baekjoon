n,m,k=map(int,input().split())
if m<=n:print(1)
elif n==1:print(2)
elif n==2:
    if k==3:print(4)
    else:print(3)
else:print(5)