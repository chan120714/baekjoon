dp=[1,1,1]
for i in range(99):
	dp.append(dp[-2]+dp[-3])
for i in range(int(input())):
	print(dp[int(input())-1])