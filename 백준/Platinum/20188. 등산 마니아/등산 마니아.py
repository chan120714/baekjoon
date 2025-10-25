import sys
input=sys.stdin.readline
sys.setrecursionlimit(323456)


n=int(input())
res=-n*(n-1)//2
g=[[]for i in range(n+1)]

for i in range(n-1):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)

def dfs(x,lst):
    global res
    t=1
    for i in g[x]:
        if i==lst:continue
        t+=dfs(i,x)
    res+=t*(t-1)//2+t*(n-t)
    return t
dfs(1,-1)
print(res)