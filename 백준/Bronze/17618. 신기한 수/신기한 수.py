s=0
for i in range(1,int(input())+1):
    a=0
    k=i
    while k:
        a+=k%10
        k//=10
    if i%a==0:
        s+=1
print(s)