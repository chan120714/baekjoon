import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
i=0
t=0
d=4
k=1
q,w,e,r=0,0,0,0
p=0
while i<n:
    if t>240:
        if p<35:
            p=0
        elif 35<=p<65:
            q+=1
        elif p<95:
            w+=1
        elif p<125:
            e+=1
        else:
            r+=1
        p=0
        k=1
        t=0
        d=4
        continue
    v=a[i]
    i+=1
    if v==1:
        if p<35:
            p=0
        elif 35<=p<65:
            q+=1
        elif p<95:
            w+=1
        elif p<125:
            e+=1
        else:
            r+=1
        p=0
        k=1
        t=0
        d=4
        continue
    elif v==2:
        if k>1:
            k//=2
        else:
            d+=2
    elif v==3:
        o=0
    elif v==4:
        t+=56
    elif v==5:
        if d>1:
            d-=1
    elif v==6:
        if k<32:
            k*=2
    p+=k
    t+=d
print(q,w,e,r,sep='\n')
