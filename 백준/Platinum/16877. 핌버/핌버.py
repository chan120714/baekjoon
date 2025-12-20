import sys
input=sys.stdin.readline
n=int(input())

f=[1,1]
for i in' '*30:f+=f[-1]+f[-2],

dp=[0]*3001231

for i in range(1,3000001):
    k=[0]*32
    for j in f:
        if i-j<0:break
        k[dp[i-j]]=1
    for j,x in enumerate(k):
        if x==0:
            dp[i]=j
            break


res=0
for i in map(int,input().split()):
    res^=dp[i]
print((0<res)*'koosaga'or'cubelover')