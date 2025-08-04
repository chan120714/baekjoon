n=int(input())
a=[list(map(str,input().split()))for i in range(n)]
k=set()
for i in ['Eastern','Central','Western']:
    p=0
    for j in range(n):
        if a[j][1]!=i:continue
        ret=2
        for t in range(j):
            if a[t][1]!=i:continue
            if a[t][2]==a[j][2]:ret=0
        if ret>0:k.add(j);p+=1
        if p==2:break
for i in range(n):
    if i in k:continue
    ret=2
    for j in k:
        if a[j][2]==a[i][2]:ret-=1
    if ret>0:k.add(i)
    if len(k)==12:break
k=list(k)
k.sort()
for i in k:print(a[i][0])