n=int(input())
res=0
for i in range(1,103101):
    k=str(i)
    p=k+k[::-1]
    if int(p)<=n:
        res+=1
    
    t=k[:-1]+k[::-1]
    if int(t)<=n:
        res+=1
print(res)
