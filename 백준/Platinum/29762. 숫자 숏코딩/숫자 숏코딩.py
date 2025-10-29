n=int(input())
res=len(str(n))
ret=[[n]]

k=[-1]*(10**8+1)
l=[]*(10**8+1)
k[1]=0

for i in range(2,int(n**.5)+1):
    t=2
    while i**t<=n:
        if k[i**t]>len(str(i))+len(str(t))+1:
            k[i**t]=len(str(i))+len(str(t))+1
            l[i**t]=(i,t)
        t+=1
for i in range(2,n//2+1):
    x=n
    if x%i:continue
    t=0
    while x%i<1:
        t+=1
        x//=i
    if x==1:
        if res>len(str(i))+len(str(t))+1:
            res=min(res,len(str(i))+len(str(t))+1)
            ret=[(i,t)]
        continue

    v=len(str(x))
    cur=[x]
    if k[x]>-1:
        if v>k[x]:
            v=min(k[x],v)
            cur=l[x]
    v+=1
    if res>len(str(i))+len(str(t))+1+v:
        res=min(res,len(str(i))+1+len(str(t))+v)
        ret=[(i,t),cur]
if len(ret)==1:
    if len(ret[0])==1:
        print(ret[0][0])
    else:
        print(ret[0][0],ret[0][1],'^')
else:
    if len(ret[0])==2 and len(ret[1])==2:
        print(ret[0][0],ret[0][1],'^',ret[1][0],ret[1][1],'^ *')
    elif len(ret[0])==2:
        print(ret[0][0],ret[0][1],'^',ret[1][0],'*')
    elif len(ret[1])==2:
        print(ret[0][0],ret[1][0],ret[1][1],'^ *')
    else:
        print(ret[0][0],ret[1][0],'*')