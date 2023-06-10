a=list(input())
b=list(input())
c,d=len(a),len(b)
e=max(c,d)
dp=[[0]*(e+1) for i in range(e+1)]
for i in range(c):
    for j in range(d):
         if a[i]==b[j]:
             dp[i+1][j+1]=dp[i][j]+1
         else:
             dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
print(max(dp[c]))