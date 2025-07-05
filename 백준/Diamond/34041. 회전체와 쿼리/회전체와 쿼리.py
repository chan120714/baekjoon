import sys
input=sys.stdin.readline
import math
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
a+=a
m=len(a)
c=[0]*(m+1)
for i in range(1,m):
    c[i]=c[i-1]+a[i-1][0]*a[i][1]-a[i][0]*a[i-1][1]
c[n]=c[n-1]+a[n-1][0]*a[0][1]-a[0][0]*a[n-1][1]

xi=[0]*(m+1)
yi=[0]*(m+1)
for i in range(1,m):
    xi[i]=xi[i-1]+(a[i-1][0]+a[i][0])*(a[i-1][0]*a[i][1]-a[i][0]*a[i-1][1])
    yi[i]=yi[i-1]+(a[i-1][1]+a[i][1])*(a[i-1][0]*a[i][1]-a[i][0]*a[i-1][1])
xi[n]=xi[n-1]+(a[n-1][0]+a[0][0])*(a[n-1][0]*a[0][1]-a[0][0]*a[n-1][1])
yi[n]=yi[n-1]+(a[n-1][1]+a[0][1])*(a[n-1][0]*a[0][1]-a[0][0]*a[n-1][1])

s=c[n]/2
cx=xi[n]/(6*s)
cy=yi[n]/(6*s)

for _ in range(int(input())):
    i,j=map(int,input().split())
    if i==j or (i+1)%n==j or (j+1)%n==i:
        print(0)
        continue
    
    if i>j:
        j+=n
    
    dx=a[i-1][0]-a[j-1][0]
    dy=a[i-1][1]-a[j-1][1]
    A=abs((c[j-1]-c[i-1]+a[j-1][0]*a[i-1][1]-a[i-1][0]*a[j-1][1]))/2
    if A==0 or abs(A-s)<1e-12:
        print(0)
        continue
    x1=xi[j-1]-xi[i-1]+(a[i-1][0]+a[j-1][0])*(a[j-1][0]*a[i-1][1]-a[i-1][0]*a[j-1][1])
    x1/=6*A
    y1=yi[j-1]-yi[i-1]+(a[i-1][1]+a[j-1][1])*(a[j-1][0]*a[i-1][1]-a[i-1][0]*a[j-1][1])
    y1/=6*A
    r1=abs(dx*(y1-a[i-1][1])-dy*(x1-a[i-1][0]))/((dx*dx+dy*dy)**.5)

    A2=s-A
    x2=(s*cx-A*x1)/A2
    y2=(s*cy-A*y1)/A2
    r2=abs(dx*(y2-a[i-1][1])-dy*(x2-a[i-1][0]))/((dx*dx+dy*dy)**.5)
    
    v1=A*math.pi*2*r1
    v2=A2*math.pi*2*r2
    print(min(v1,v2))