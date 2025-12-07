n,d,s=map(int,input().split())
n//=s
d//=s
if d==0:
    print(s)
    exit()
k=1
y=min(d*2,n)
if y%2<1:r=y
else:
    o=0
    if y-1<=d:o=1
    else:
        for i in range(2,int(y**.5)+1):
            if y%i<1:
                a1,a2=i,y//i
                if y-a1<=d:
                    o=1
                    break
                elif y-a2<=d:
                    o=1
                    break
    if o:r=y
    else:r=y-1
print(r*s)