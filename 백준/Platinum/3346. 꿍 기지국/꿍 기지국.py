import sys
input=sys.stdin.readline

n,l=map(int,input().split())


def inte(a1,b1,a2,b2):
    return (b2-b1)/(a1-a2)




ms=[]
bs=[]
xs=[]

prev=1e30
bst=1e30


def add():

    
    m=-2*prev

    b=prev*prev+bst
    
    if ms and abs(m-ms[-1])<1e-9:
        if b<bs[-1]:
            ms.pop()
            bs.pop()
            xs.pop()
        else:
            return

    while ms:
        xi=inte(ms[-1],bs[-1],m,b)
        if xi<=xs[-1]:
            ms.pop()
            bs.pop()
            xs.pop()
        else:
            break


    if not ms:
        xs.append(-1e20)
    else:
        xs.append(inte(ms[-1],bs[-1],m,b))

    ms.append(m)
    bs.append(b)

for i in range(n):
    x,y=map(int,input().split())


    if prev==1e30:
        prev=x
        bst=y*y
    elif x==prev:
        bst=min(y*y,bst)
    else:
        add()
        prev=x
        bst=y*y
add()
res=0
M=len(ms)
    
for i in range(M):
    le=xs[i]
    ri=l if i==M-1 else xs[i+1]

    le=max(0,le)
    ri=min(ri,l)
    if le>ri:continue
    res=max(res,le*le+ms[i]*le+bs[i],ri*ri+ms[i]*ri+bs[i])
    
print(res**.5)