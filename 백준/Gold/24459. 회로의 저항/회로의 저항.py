import sys
input=sys.stdin.readline
sys.setrecursionlimit(304035)

n=int(input())
g=[[]for i in range(n+1)]

for i in range(n-1):
    p,q,w=map(int,input().split())
    g[p].append((q,w))
    g[q].append((p,w))

res1=1e18
res2=-1e18
def dfs(x,lst,v,k):
    global res1,res2
    ret=[0]
    for i in g[x]:
        if i[0]!=lst:
            t=dfs(i[0],x,i[1],k+i[1])
            ret.append(t)
    ret.sort()
    if len(ret)>1:
        res2=max(res2,ret[-1]+max(k,ret[-2]))
    return ret[-1]+v

def dfs1(x,lst,v,k):
    global res1,res2
    ret=[1e18]
    for i in g[x]:
        if i[0]!=lst:
            t=dfs1(i[0],x,i[1],k+i[1])
            ret.append(t)
    ret.sort(reverse=True)
    if len(ret)>1:
        res1=min(res1,ret[-1]+min(k,ret[-2]))
    else:
        res1=min(res1,k)
        return v
    return ret[-1]+v

for i in range(n):
    if len(g[i])==1:
        dfs(i,-1,0,0)
        dfs1(i,-1,0,0)
        break
print(res2,res1,sep='\n')