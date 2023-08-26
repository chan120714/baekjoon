import sys
input=sys.stdin.readline

a=[1]*4000002
a[0]=0
dp=[]
for i in range(1,4000002):
    if a[i]==1:
        dp.append(i+1)
        t=i
        t+=i+1
        while t<4000001:
            a[t]=0
            t+=i+1
ddp=[0]*(len(dp))
ddp[1]=2
for i in range(2,len(dp)):
    ddp[i]=ddp[i-1]+dp[i-1]
n=int(input())
k=len(ddp)
st,ed=0,0
l=0
dp.append(10000000)
t=0
while dp[ed-t]<=n and k>ed:
    if ddp[ed]-ddp[st]<n:
        ed+=1
    elif ddp[ed]-ddp[st]>n:
        st+=1
    else:
        l+=1
        ed+=1
    t=1
print(l)