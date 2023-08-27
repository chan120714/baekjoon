import sys
input=sys.stdin.readline
a=[1]*3000002
a[0]=0
d=[]
for i in range(1,3000002):
    if a[i]==1:
        d.append(i+1)
        t=i
        t+=i+1
        while t<3000001:
            a[t]=0
            t+=i+1
dp=[0]*3000003
dp[2]=1
dp[3]=1
for i in d[2:]:
    n,m=i//2,i//2
    while n>0:
        if a[n-1]==1 and a[m-1]==1:
            dp[i]=dp[n]+dp[m]+1
            break
        else:
            n-=1
            m+=1
print(dp[int(input())])