dp=[0]
for i in range(1,447):
    for j in range(i+1):dp+=i,

input()
s=0
for i in map(int,input().split()):
    s^=dp[i]
print('koosaga'if s else'cubelover')