import sys
from collections import deque
input=sys.stdin.readline

n,m,r=map(int,input().split())
graph=[[]for i in range(n+1)]
visit=[0 for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
q=deque()
q.append((r,0))
v=[-1 for i in range(n+1)]
c=1
while q:
    x,y=q.popleft()
    visit[x]=c
    c+=1
    v[x]=y
    for i in graph[x]:
        if visit[i]==0:
            visit[i]=1
            q.append((i,y+1))
s=0
for i in range(1,n+1):
    s+=v[i]*visit[i]
print(s)