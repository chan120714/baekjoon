a=int(input())
graph=list(map(int,input().split()))
dp=[graph[0]]
for i in graph:
    if i>dp[-1]:
        dp.append(i)
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
        else:
            dp[md+1]=i
print(len(dp))