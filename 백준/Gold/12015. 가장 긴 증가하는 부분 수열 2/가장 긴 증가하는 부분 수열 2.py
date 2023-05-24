import sys
input=sys.stdin.readline
a=int(input())
k=list(map(int,input().split()))
dp=[k[0]]
for i in k[0:]:
    st,ed=0,len(dp)
    if i> dp[-1]:
        dp.append(i)
    else:
        while st<ed:
            m=(st+ed)//2
            if dp[m]<i:
                st=m+1
            else:
                ed=m
        if dp[m]>=i:
            dp[m]=i
        else:
            dp[m+1]=i
print(len(dp))