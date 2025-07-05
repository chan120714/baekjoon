def ipow(a,x,mod):
    res=1
    while x:
        if x&1:
            res*=a
            res%=mod
        a*=a
        a%=mod
        x>>=1
    return res

for i in range(1,int(input())+1):
    a,p=map(int,input().split())
    a%=p
    t=ipow(a,(p-1)//2,p)
    res=1 if t==1 else -1
    print(f'Scenario #{i}:\n{res}\n')