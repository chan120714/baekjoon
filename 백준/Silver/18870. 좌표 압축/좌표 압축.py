import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int,input().split()))
c=list(set(b))
c.sort()
for i in range(a):
    mi=0
    ma=len(c)-1
    md=(mi+ma)//2
    while b[i]!=c[md]:
        if b[i]>c[md]:
            mi=md+1
        else:
            ma=md-1
        md=(mi+ma)//2
    print(md,end=' ')