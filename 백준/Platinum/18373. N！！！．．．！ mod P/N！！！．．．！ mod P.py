from math import factorial

res=1

n,k,p=map(int,input().split())

if n==2:
    print(2%p)
    exit()
if k>=3 or n>=p:
    if k==3 and n==3:
        res=1
        for i in range(1,721):
            res*=i
            res%=p
        print(res)
    else:
        print(0)
    exit()
if n>=13:
    print(0)
    exit()

#이하 n<13, k=2인 케이스 
t=factorial(n)
if t>=p:
    print(0)
    exit()
if n==12:
    res=1
    for i in range(t+1,p-1):
        res*=i
        res%=p
    print(pow(res,-1,p))
else:
    res=1
    for i in range(1,t+1):
        res*=i
        res%=p
    print(res)