import sys
input=sys.stdin.readline
from math import*
INF=1e9
n=int(input())
graph=[[INF for i in range(n+1)]for i in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
t=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if t[i][j]==1:
            graph[i+1][j+1]=1


for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if graph[j][k]==0:
                graph[j][k]=graph[j][i]+graph[i][k]
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if 1<=graph[i][j]<INF:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()