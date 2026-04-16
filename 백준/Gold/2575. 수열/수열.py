n=int(input())
if n==1:
    print(1,1)
    exit()
print((n+2)//3,end=' ') 
x=0
while n%4 == 0:
    n//=4
    x+=1
for i in range(2,1000000):
    while n%i==0:
        n//=i
        x+=1
print(x)
