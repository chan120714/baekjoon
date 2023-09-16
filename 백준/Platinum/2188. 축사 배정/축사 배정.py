import sys
input=sys.stdin.readline
n,m=map(int,input().split())
select=[0]*(m+1)
graph=[[] for i in range(n+1)]
for i in range(1,n+1):
    l,*graph[i]=(map(int,input().split()))

def dfs(n):
    if visit[n]==True:
        return False
    visit[n]=True
    for j in graph[n]:
        if select[j]==0 or dfs(select[j]):
            select[j]=n
            return True
    return False

for i in range(1,n+1):
    visit=[False]*(n+1)
    dfs(i)

res=0
for i in range(1,m+1):
    if select[i]>0:
        res+=1
print(res)