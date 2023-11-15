a=sorted(list(map(int,input().split())))
n=list(map(ord,input()))
for i in n:
    print(a[i-65],end=' ')