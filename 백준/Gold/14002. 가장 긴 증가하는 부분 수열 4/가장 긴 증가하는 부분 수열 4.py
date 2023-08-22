a=int(input())
graph=list(map(int,input().split()))
dp=[graph[0]]
ddp=[0 for i in range(a)]
p=0
for i in graph:
    if i>dp[-1]:
        dp.append(i)
        ddp[p]=len(dp)
    else:
        st,ed=0,len(dp)
        while st<ed:
            md=(st+ed)//2
            if dp[md]<i:
                st=md+1
            else:
                ed=md
        if dp[md]>=i:
            dp[md]=i
            ddp[p]=md+1
        else:
            dp[md+1]=i
            ddp[p]=md+2
    p+=1
ddp[0]=1
print(len(dp))
t=len(dp)
rr=[]
for i in range(a-1,-1,-1):
    if ddp[i]==t:
        rr.append(graph[i])
        t-=1
rr.reverse()
print(*rr)