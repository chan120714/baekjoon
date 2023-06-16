a=int(input())
b=list(map(int,input().split()))
c=[]
s=0
t=0
for i in range(a):
    if b[i]%2==0:
        s+=b[i]
    else:
        c.append(b[i])
d=(len(c))//2
if d>0:
    c.sort(reverse=True)
    s+=sum(c[:d*2])
print(s)