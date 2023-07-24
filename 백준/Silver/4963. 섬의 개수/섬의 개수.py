import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(x,y):
    if x<=-1 or y<=-1 or x>=m or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y-1)
        dfs(x-1,y)
        dfs(x-1,y+1)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y-1)
        dfs(x+1,y)
        dfs(x+1,y+1)
        return True
    return False
while True:
    k=0
    n,m=map(int,input().split())
    if n+m==0:
        break
    graph=[list(map(int,input().split())) for i in range(m)]
    for i in range(m):
        for j in range(n):
            if dfs(i,j)==True:
                k+=1
    print(k)