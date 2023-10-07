import sys
input=sys.stdin.readline
from collections import deque
q=deque()
n,m=map(int,input().split())
if n==m:
    print(0)
    exit()
graph=[[0,0] for i in range(500001)]
q.append(n)
dx=[-1,1,2]
t=1
r=1
graph[n][0]=1
while q:
    for _ in range(len(q)):
        x=q.popleft()
        for i in dx:
            if i!=2:
                fx=x+i
            else:
                fx=x*2
            if fx<0 or 500000<fx:
                continue
            if graph[fx][r]!=0:
                continue
            graph[fx][r]=graph[x][-r]+1
            q.append(fx)
    m+=t
    if m>500000:
        print(-1)
        exit()
    if graph[m][r]!=0:
        break
    t+=1
    r+=1
    r%=2
print(t)
