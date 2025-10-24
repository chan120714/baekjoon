a,b,c=map(int,input().split())
f=lambda A,B:abs(A-a)+abs(B-b)+abs(A*B-c)
res=f(a,b)
for i in range(1,int(c**.5)+1):
    t,p=c//i,(c+i-1)//i
    res=min(res,f(i,t),f(t,i),f(p,i),f(i,p))
res=min(res,f(a,c//a+1))
if c//a>0:res=min(res,f(a,c//a))
if c//a>1:res=min(res,f(a,c//a-1))

res=min(res,f(c//b+1,b))
if c//b>0:res=min(res,f(c//b,b))
if c//b>1:res=min(res,f(c//b-1,b))

print(res)