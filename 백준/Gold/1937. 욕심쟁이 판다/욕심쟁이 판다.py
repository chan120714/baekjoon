import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
n=int(input())
a=[list(map(int,input().split()))for i in range(n)]
dp=[[0]*n for i in range(n)]

res=0
def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    cur=1
    for i in ((-1,0),(1,0),(0,1),(0,-1)):
        dx=x+i[0]
        dy=y+i[1]
        if 0<=dx<n and 0<=dy<n:
            if a[x][y]<a[dx][dy]:
                cur=max(cur,1+dfs(dx,dy))
    dp[x][y]=cur
    return cur


res=0
for i in range(n):
    for j in range(n):
        res=max(res,dfs(i,j))
print(res)
