n=['N','E','S','W']
s=0
for i in range(10):
    a=int(input())
    if a==1:
        s+=1
    elif a==2:
        s+=2
    else:
        s-=1
    if s<0:
        s+=4
s%=4
print(n[s])