import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
a=int(input())
graph=[list(map(str,input())) for i in range(a)]
visit=[[0 for i in range(a)]for i in range(a)]
def dfs(x,y,g):
    if x<0 or x>=a or y<0 or y>=a:
        return False
    if visit[x][y]==1:
        return False
    if graph[x][y]==g:
        visit[x][y]=1
        dfs(x+1,y,g)
        dfs(x-1,y,g)
        dfs(x,y+1,g)
        dfs(x,y-1,g)
        return True
    
def dfs1(x,y,g):
    if x<0 or x>=a or y<0 or y>=a:
        return False
    if graph[x][y]==g:
        graph[x][y]=0
        dfs1(x+1,y,g)
        dfs1(x-1,y,g)
        dfs1(x,y+1,g)
        dfs1(x,y-1,g)
        return True
l,k=0,0
RGB=['R','G','B']

gr=graph

for _ in RGB:
    for i in range(a):
        for j in range(a):
            if dfs(i,j,_)==True:
                l+=1
                
for i in range(a):
    for j in range(a):
        if gr[i][j]=='G':
            gr[i][j]='R'
for _ in RGB:
    for i in range(a):
        for j in range(a):
            if dfs1(i,j,_)==True:
                k+=1
print(l,k)