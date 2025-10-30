for i in range(int(input())):
    n,m=map(int,input().split())
    x=n-m
    y=(m-1)//2
    if x&y==0:
        print(1)
    else:
        print(0)