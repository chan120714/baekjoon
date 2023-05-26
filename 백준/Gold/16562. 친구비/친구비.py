import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
n,m,k=map(int,input().split())
ai=list(map(int,input().split()))
graph=[[] for i in range(n+1)]
visit=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b);graph[b].append(a)
df=[]
def dfs(v):
    visit[v]=1
    df.append(ai[v-1])
    for i in graph[v]:
        if visit[i]==0:
            dfs(i)
l=1
s=0
while sum(visit)!=n:
    df=[]
    if visit[l]!=1:
        dfs(l)
        s+=min(df)
    l+=1
if s<=k:
    print(s)
else:
    print('Oh no')