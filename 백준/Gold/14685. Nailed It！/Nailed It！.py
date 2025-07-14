import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

cnt=[0]*2012
for i in a:
    cnt[i]+=1

maxl=0
c=0

for i in range(2,4001):
    cur=0
    for j in range(1,i//2+1):
        y=i-j
        if j==y:
            cur+=cnt[j]//2
        else:
            if y>2000:
                continue
            cur+=min(cnt[j],cnt[y])

    if cur>maxl:
        maxl=cur
        c=1
    elif cur==maxl:
        c+=1
print(maxl,c)