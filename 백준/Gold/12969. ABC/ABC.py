n,k=map(int,input().split())
r=-1
t={0}
def f(s,a,b,c,d):
 global r,t
 if(a,b,c,d)in t or-1!=r or k<d or a+b+c>n:return
 if d==k:r=s+(n-len(s))*'A';return
 f(s+'A',a+1,b,c,d);f(s+'B',a,b+1,c,d+a);f(s+'C',a,b,c+1,d+a+b);t|={(a,b,c,d)}
f('',0,0,0,0)
print(r)