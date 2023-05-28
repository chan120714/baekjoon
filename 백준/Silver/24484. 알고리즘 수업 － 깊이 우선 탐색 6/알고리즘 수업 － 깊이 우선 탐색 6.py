import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for i in range(n+1)]
visit=[-1]*(n+1)
vi=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b);graph[b].append(a)
for i in range(n+1):
    graph[i].sort(reverse=True)
d=1
def dfs(v,c):
    global d
    vi[v]=d
    d+=1
    visit[v]=c
    for i in graph[v]:
        if visit[i]==-1:
            dfs(i,c+1)
dfs(v,0)
res=0
for i in range(1,n+1):
    res+=visit[i]*vi[i]
print(res)