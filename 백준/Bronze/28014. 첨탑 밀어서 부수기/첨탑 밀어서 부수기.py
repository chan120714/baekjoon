a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    if i==0:
        c+=1
    elif b[i]>=b[i-1]:
        c+=1
print(c)