from math import*
r,s,h=map(int,input().split())
t=0
if (2*r*pi/(s*h))%1>=0.5:
    t=-1
else:
    t=1
day=(2*r*pi/(s*h))//1
if t==-1:
    day+=1
day=int(day)
res=[]
v=1e9
for i in range(2,1001):
    for j in range(i+1,1001):
        if j%i:continue
        for k in range(j+1,1001):
            if k%j:continue
            x=day+t*(1/i-1/j+1/k)
            if abs(x-(2*r*pi/(s*h)))<v:
                v=abs(x-(2*r*pi/(s*h)))
                res=(i,j,k)
print(*res)
