
def ori(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def f(a,b):
    if a==0 and b==0: return 1
    if a*b>0: return 1
    return 0
while 1:
    a1,b1,c1=map(int,input().split())
    if a1+b1+c1==0:break

    a2,b2,c2=map(int,input().split())
    a3,b3,c3=map(int,input().split())
    a,b,c=map(int,input().split())


    if ori((a1,b1),(a2,b2),(a3,b3))==0:
        if (a1,b1)==(a2,b2)==(a3,b3):
            if (a,b)==(a1,b1):
                print("YES")
            else:
                print("NO")
            continue
        U=(a1,b1)
        V=(a2,b2)
        if U==V:
            V=(a3,b3)
        if ori(U,V,(a,b)):
            print("NO")
            continue

        ist=0
        minx,maxx=min(a1,a2,a3),max(a1,a2,a3)
        miny,maxy=min(b1,b2,b3),max(b1,b2,b3)
        
        if minx!=maxx:
            if minx<a<maxx:
                ist=1
        else:
            if miny<b<maxy:
                ist=1
        if ist:
            print("YES")
        else:
            print("NO")
    else:
        A=(a1,b1)
        B=(a2,b2)
        C=(a3,b3)
        D=(a,b)
        o1,o2,o3=ori(A,B,D),ori(B,C,D),ori(C,A,D)
        ist=1
        if o1==0 or o2==0 or o3==0 or f(o1,ori(A,B,C))==0 or f(o2,ori(B,C,A))==0 or f(o3,ori(C,A,B))==0:ist=0
        if ist:
            print("YES")
        else:
            print("NO")
    input()
