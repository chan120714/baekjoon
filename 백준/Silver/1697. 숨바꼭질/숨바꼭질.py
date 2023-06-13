import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
graph=[0 for i in range(1000001)]
graph[n]=1
queue=deque()
queue.append(n)
while graph[m]==0:
    x=queue.popleft()
    nx=x+1
    if nx>1000000:
        continue
    else:
        if graph[nx]==0:
            graph[nx]=graph[x]+1
            queue.append(nx)
    nx=x-1
    if nx<0:
        continue
    else:
        if graph[nx]==0:
            graph[nx]=graph[x]+1
            queue.append(nx)
    nx=x*2
    if nx>1000000:
        continue
    else:
        if graph[nx]==0:
            graph[nx]=graph[x]+1
            queue.append(nx)
print(graph[m]-1)