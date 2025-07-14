import sys
input=sys.stdin.readline

from collections import *

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

while 1:
    n,m,k,l=map(int,input().split())
    if n+m+k+l==0:
        break

    a=[]
    for i in range((l-1)//10+1):
        t=list(map(int,input().split()))
        a.extend(t)
    
    g=[[[0 for i in range(n+2)]for i in range(m+2)]for i in range(k+2)]

    vi=[[[0 for i in range(n+2)]for i in range(m+2)]for i in range(k+2)]
    
    for i in a:
        g[i//(n*m)+1][i//n%m+1][i%n+1]=1
        
    res=0

    q=deque([(0,0,0)])
    vi[0][0][0]=1
    while q:
        z,y,x=q.popleft()
        for i in range(6):
            fz,fy,fx=z+dz[i],y+dy[i],x+dx[i]
            if not (0<=fz<=1+k and 0<=fy<=1+m and 0<=fx<=1+n):
                continue
            if vi[fz][fy][fx]:
                continue
            if g[fz][fy][fx]==1:
                res+=1
            else:
                vi[fz][fy][fx]=1
                q.append((fz,fy,fx))
    print(f'The number of faces needing shielding is {res}.')