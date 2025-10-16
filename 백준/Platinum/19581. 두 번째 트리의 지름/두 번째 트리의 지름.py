import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
n=int(input())
graph=[[]for i in range(n+1)]
for i in range(n-1):
	a,b,c=map(int,input().split())
	graph[a].append((b,c))
	graph[b].append((a,c))
visit=[-1]*(n+1)
res=0
node=0
def dfs(n,dist):
	global res,node
	visit[n]=dist
	if dist>res:
		res=dist
		node=n
	for i in graph[n]:
		if visit[i[0]]==-1:
			dfs(i[0],i[1]+dist)
dfs(1,0)
visit=[-1]*(n+1)
res=0
dfs(node,0)
visit.sort()
ret=[]
ret.append(visit[-2])

visit=[-1]*(n+1)

dfs(node,0)
visit.sort()
ret.append(visit[-2])
ret.sort()
print(max(ret))
