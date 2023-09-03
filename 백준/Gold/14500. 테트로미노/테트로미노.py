import sys
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(n)]
ss=0
visit=[[0for i in range(m)]for i in range(n)]
def dfs(x,y,c,s):
	global ss
	
	if c==4:
		ss=max(ss,s)
		return
	
	for i in range(4):
		fx=dx[i]+x
		fy=dy[i]+y
		if 0<=fx<n and 0<=fy<m and visit[fx][fy]==0:
			visit[fx][fy]=1
			dfs(fx,fy,c+1,s+graph[fx][fy])
			visit[fx][fy]=0

def tspin(x,y):
	global ss
	
	for i in range(4):
		xy=graph[x][y]
		for j in range(3):
			k=(i+j)%4
			fx=x+dx[k]
			fy=y+dy[k]
			if fx<0 or fx>=n or fy<0 or fy>=m:
				xy=0
				break
			xy+=graph[fx][fy]
		ss=max(ss,xy)
for i in range(n):
	for j in range(m):
		visit[i][j]=1
		dfs(i,j,1,graph[i][j])
		tspin(i,j)
		visit[i][j]=0
print(ss)