n,d=map(int,input().split())

g=[[]for i in range(d+1)]

for i in range(n):
    s,e,w=map(int,input().split())
    if e>d:
        continue
    if e-s<=w:
        continue
    g[s].append((e,w))

INF=1e18

dist=[INF]*-~d
dist[0]=0

for i in range(d):
    dist[i+1]=min(dist[i+1],dist[i]+1)

    for e,w in g[i]:
        dist[e]=min(dist[e],dist[i]+w)
print(dist[d])