n=int(input())
res=[0]*-~n

for i in range(1,n+1):
    *a,=map(int,input().split())
    cur=0
    for j in a[2:]:
        if res[j]>cur:
            cur=res[j]
    res[i]=cur+a[0]
print(max(res))