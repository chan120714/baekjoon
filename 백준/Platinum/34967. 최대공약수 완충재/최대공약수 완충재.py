n=int(input())

d=[]
for i in range(1,n):
    if i%2:
        d.append(n-1-(i-1)//2)
    else:
        d.append(i//2)
        
a=[0]*n
a[0]=d[0]
for i in range(1,n-1):
    a[i]=d[i-1]*d[i]
a[n-1]=d[n-2]
print(*a)