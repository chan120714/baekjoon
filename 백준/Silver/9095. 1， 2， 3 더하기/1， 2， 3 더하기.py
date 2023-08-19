a=int(input())
dp=[1,2,4]
for i in range(10):
    dp.append(dp[-1]+dp[-2]+dp[-3])
for i in range(a):
    n=int(input())
    print(dp[n-1])