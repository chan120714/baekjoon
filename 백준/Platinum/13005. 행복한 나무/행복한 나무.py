import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))

res=0
g=[[]for i in range(n+1)]
for i in range(2,n+1):
    x,y=map(int,input().split())
    g[i].append((x,y))
    g[x].append((i,y))
def dfs(x,lst,dist,t):
    global res
    if a[x-1]<dist:
        t=-1
    if t==-1:
        res+=1
    for i in g[x]:
        if i[0]==lst:continue
        dfs(i[0],x,max(dist+i[1],i[1]),t)

dfs(1,-1,-1e9,0)
print(res)