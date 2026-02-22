n=int(input())

a=[input()for i in range(n)]
s=set()
res=0
i=0
for _ in range(n):
    x=input()

    while i<n and a[i] in s:
        i+=1
    if i<n and x==a[i]:
        i+=1
        s.add(x)
    else:
        res+=1
        s.add(x)
print(res)