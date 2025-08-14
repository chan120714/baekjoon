import sys
input=sys.stdin.readline
m=int(input())
n=list(map(int,input().split()))
a=list(map(int,input().split()))

for i in range(m):
    x=n[i]
    z=a[i]
    if z==0:
        print(0,end=' ')
        continue
    if x==1:
        print(1,end=' ')
        continue
    st=0
    ed=10**9+7
    res=10**9+7
    while st<=ed:
        mid=(st+ed)>>1
        cur=mid
        temp=mid//x #덤 개수
        cur+=temp
        tempx=mid%x #남은거
        while temp+tempx>=x:
            cur+=(tempx+temp)//x
            temp,tempx=(tempx+temp)//x,(tempx+temp)%x
        if cur>=z:
            res=min(res,mid)
            ed=mid-1
        else:
            st=mid+1
    print(res,end=' ')