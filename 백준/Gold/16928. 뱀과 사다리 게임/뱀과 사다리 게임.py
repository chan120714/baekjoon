import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
graph=[0 for i in range(101)]
node=[[0 for i in range(101)]for i in range(101)]
for i in range(n):
    a,b=map(int,input().split())
    node[a][b]=1
for i in range(m):
    a,b=map(int,input().split())
    node[a][b]=1
graph[1]=1
q=deque()
q.append(1)
while q:
    x=q.popleft()
    for i in range(1,7):
        dx=x+i
        if dx<0 or dx>100:
            continue
        if graph[dx]!=0:
            continue
        graph[dx]=graph[x]+1
        if sum(node[dx][0:])!=0:
            for j in range(101):
                if node[dx][j]==1:
                    if graph[j]==0:
                        q.append(j)
                        graph[j]=graph[dx]
                        break
        else:
            q.append(dx)
print(graph[-1]-1)