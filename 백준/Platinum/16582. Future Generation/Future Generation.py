import sys
input=sys.stdin.readline
 
n=int(input())
a=[input().rstrip() for i in range(n)]
 
dp=[[0 for i in range(32768)] for i in range(n)]
 
def make(a):
    s=['']
    for i in a:
        s+=[x+i for x in s]
    s=sorted(list(set(s[1:])))
 
    return s
 
k=make(a[0])
for i in range(len(k)):
    dp[0][i]=len(k[i])
 
for i in range(1,n):
    k=make(a[i])
    prev=make(a[i-1])
    pv=len(prev)
    mv=-1
    t=0
    for j in range(len(k)):
        while t<pv and prev[t]<k[j]:
            if dp[i-1][t]!=-1 and dp[i-1][t]>mv:
                mv=dp[i-1][t]
            t+=1
        if mv==-1:
            dp[i][j]=-1
        else:
            dp[i][j]=mv+len(k[j])
    if mv==-1:
        print(-1)
        exit()
 
print(max(dp[n-1]))