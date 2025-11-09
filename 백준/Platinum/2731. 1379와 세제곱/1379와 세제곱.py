for s in open(0).read().split()[1:]:
 t,x,p=int(s),0,1
 for _ in s:
  q=p;p*=10;u=t%p
  for d in range(10):
   c=x+d*q
   if pow(c,3,p)==u:x=c;break
 print(x)