n,m=input().split()
if n==m:
    print(1)
    exit()
res=-1
for i in range(1,101):
    k=''
    for j in range(10):
        t=n.count(str(j))
        if t==0:continue
        k+=str(t)
        k+=str(j)

    if k==m:
        res=i
        break
    n=k
print(res+1 if res>0 else "Does not appear")