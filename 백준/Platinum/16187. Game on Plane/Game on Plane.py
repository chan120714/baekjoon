import sys
input=sys.stdin.readline
dp=[0]*5010
for i in range(2,5001):
    cnt=[0]*5010
    for j in range(i-1):
        cnt[dp[j]^dp[i-j-2]]+=1
    for j in range(5010):
        if cnt[j]==0:
            dp[i]=j
            break
for i in range(int(input())):
    print('Second' if dp[int(input())]==0 else 'First')