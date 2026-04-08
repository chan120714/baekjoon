n,*a=map(int,open(0).read().split())
s=[0]
c=w=p=0
for x in[*map(lambda x:(x-20)//10,a),0]:
 w+=abs(x-p);p=x
 while s[-1]>x:
  t=s.pop();c+=(t-max(s[-1],x)+3)//4
 if s[-1]<x:s+=x,
print(w*10,c*4)