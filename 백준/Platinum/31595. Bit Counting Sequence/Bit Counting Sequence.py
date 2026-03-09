import sys
input=sys.stdin.readline



def f(a):
    n=len(a)
    if n==1:
        if a[0]<0:
            return -1
        return (1<<a[0])-1
    
    if any(v<0 for v in a):
        return -1
    res=-1
    #case 1. 2|x

    ret=1

    for i in range(0,n-1,2):
        if a[i+1]!=a[i]+1:
            ret=0
            break
    if ret:
        y=f(a[::2])
        if y!=-1:
            res=2*y
    
    ret=1
    for i in range(1,n-1,2):
        if a[i+1]!=a[i]+1:
            ret=0
            break
    if ret:
        temp=[a[0]-1]+a[1::2]
        y=f(temp)
        if y!=-1:
            k=2*y+1
        
            if res==-1 or k<res:
                res=k

    return res
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(f(a))
