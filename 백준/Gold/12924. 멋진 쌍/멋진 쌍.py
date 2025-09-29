n,m=map(int,input().split())

res=0

for i in range(n,m+1):
    i=str(i)
    k=[]
    for j in range(len(i)):
        k.append(i[j:]+i[:j])
    i=int(i)
    k=list(set(k))
    for j in k:
        if i<int(j)<=m:
            res+=1
print(res)
