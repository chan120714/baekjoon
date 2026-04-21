a=input()
b=0
for i in range(len(a)):
    if a[i]!=a[len(a)-1-i]:
        b+=1
if b==0:
    print(1)
else:
    print(0)