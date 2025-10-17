def manachers(s, n):
    t='#'+'#'.join(s)+'#'
    N=2*n+1
    a=[0]*N
    r=0
    p=0
    for i in range(N):
        if i<r:
            a[i]=min(a[2*p-i],r-i)
        while i-a[i]-1>=0 and i+a[i]+1<N and t[i-a[i]-1]==t[i+a[i]+1]:
            a[i]+=1
        if i+a[i]>r:
            r=i+a[i]
            p=i
    return a

a=input()
k=manachers(a,len(a))
res=0
for i in k:
    res+=(i+1)//2
print(res)