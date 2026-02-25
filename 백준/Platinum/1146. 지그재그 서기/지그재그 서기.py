n=int(input())
m=10**6
u=[1]
d=[1]
for i in range(2,n+1):
    u,d=[sum(d[:j])%m for j in range(i)],[sum(u[j:])%m for j in range(i)]
print(sum(u+d)%m-(n==1))