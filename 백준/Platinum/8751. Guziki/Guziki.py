import sys
input=sys.stdin.readline
import math
def r(b):
    t=[True for i in range(b+1)]

    for i in range(2,int(math.sqrt(b)+1)):
        if t[i]==True:
            j=2
            while i*j<=b:
                t[i*j]=False
                j+=1
    return[i for i in range(2,b+1) if t[i]]
b=r(2000000)
a=[i for i in range(2012031)]

for i in b:
    a[i]=i-1
    j=i+i
    while j<=2000000:
        a[j]//=i
        a[j]*=i-1
        j+=i
res=0
n,g=map(int,input().split())
if n==g:print(4)
elif g==1:print(-1)
elif g%2==0:print(0)
else:
    n=(n-1)//2
    st=n
    ed=1
    g=(g-1)//2
    for i in range(1,n+1):
        if n//i==g:
            st=min(st,i)
            ed=max(ed,i)
    res=0
    for i in range(st,ed+1):
        res+=a[i]
    res*=4
    if res>10**12:
        print(-1)
    else:
        print(res)