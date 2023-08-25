import sys
input=sys.stdin.readline
a=int(input())
graph=[list(map(int,input().split())) for i in range(a)]
graph.sort()
dp=[graph[0][1]]
ddp=[0 for i in range(a)]
p=0
for i in graph:
    if i[1]>dp[-1]:
        dp.append(i[1])
        ddp[p]=len(dp)
    else:
        st,ed=0,len(dp)
        while st<ed:
            md=(st+ed)//2
            if dp[md]<i[1]:
                st=md+1
            else:
                ed=md
        if dp[md]>=i[1]:
            dp[md]=i[1]
            ddp[p]=md+1
        else:
            dp[md+1]=i[1]
            ddp[p]=md+2
    p+=1
ddp[0]=1
t=len(dp)
rr=[]
for i in range(a-1,-1,-1):
    if ddp[i]!=t:
        rr.append(graph[i][0])
    else:
        t-=1
rr.sort()
print(len(rr))
for i in rr:
    print(i)