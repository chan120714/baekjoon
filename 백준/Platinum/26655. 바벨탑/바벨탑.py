s=[0]
c=w=p=0
for x in*map(int,open(0).read().split()[1:]),20:
 x=x//10-2;w+=abs(x-p);p=x
 while x<s[-1]:c+=(s.pop()-max(s[-1],x)+3)//4
 if x-s[-1]:s+=x,
print(w*10,c*4)