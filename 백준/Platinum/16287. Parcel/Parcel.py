import sys
input=sys.stdin.readline
w,n=map(int,input().split())
*a,=map(int,input().split())
d=dict()
for i in range(n):
    for j in range(i+1,n):
        t=a[i]+a[j]
        if t in d:
            continue
        else:
            d[t]=(i,j)
res=0
for i in range(n):
    for j in range(i+1,n):
        t=a[i]+a[j]
        k=w-t
        if k in d:pass
        else:continue
        if len({i,j}|set(d[k]))==4:
            res=1
            break
    if res:
        break
print('YNEOS'[res^1::2])