b=0
a=list(map(int,input()))
if len(a)==1:
    b-=1
while sum(a)>=10:
    c=str(sum(a))
    a=[]
    for i in range(len(c)):
        a.append(int(c[i]))
    b+=1
print(b+1)
print(["NO","YES"][sum(a)%3==0])