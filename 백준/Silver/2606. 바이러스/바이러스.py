import sys
input=sys.stdin.readline
a=int(input())
graph=[[0 for i in range(a+1)] for i in range(a+1)]
visit=[0 for o in range(a+1)]
for i in range(int(input())):
    n,m=map(int,input().split())
    graph[n][m],graph[m][n]=1,1
k=[]
def dfs(v):
    visit[v]=1
    for i in range(a+1):
        if visit[i]==0 and graph[v][i]==1:
            k.append(v)
            dfs(i)
dfs(1)
print(len(k))