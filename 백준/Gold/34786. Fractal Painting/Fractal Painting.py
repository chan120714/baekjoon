import sys
input=sys.stdin.readline

def ccw(x,y,z):
    return (y[0]-x[0])*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0])

for __ in range(int(input())):
    x0,y0,x1,y1,x2,y2=map(int,input().split())
    A=x0**2+y0**2
    B=(x0-x1)**2+(y0-y1)**2
    C=(x0-x2)**2+(y0-y2)**2
    if max(B,C)<A:
        print("YES")
    elif max(B,C)>A:
        print("NO")
    else:
        if B==A:
            if ccw((0,0),[x0,y0],(x1,y1))==0:
                print("NO")
                continue
        if C==A:
            if ccw((0,0),[x0,y0],(x2,y2))==0:
                print("NO")
                continue
        if B==C==A:
            print('NO')
            continue

        print("YES")