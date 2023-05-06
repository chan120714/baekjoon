import sys
input=sys.stdin.readline
a,n,m=map(int,input().split())
graph=list(map(int,input().split()))
tot=0
for i in range(a):
    if n<=m:
        print(sum(graph)*n)
        exit()
    if i==a-1:
        tot+=graph[i]*n
    elif i==a-2:
        while graph[i]!=0:
            if graph[i+1]!=0:
                if graph[i]>=graph[i+1]:
                    graph[i]-=graph[i+1]
                    tot+=graph[i+1]*(n+m)
                    graph[i+1]=0
                else:
                    graph[i+1]-=graph[i]
                    tot+=graph[i]*(n+m)
                    graph[i]=0
            else:
                tot+=graph[i]*n
                graph[i]=0
    else:
        while graph[i]>0:
            if graph[i+1]!=0 and graph[i+2]!=0:
                if graph[i+1]>graph[i+2]:
                    if graph[i]>=graph[i+1]-graph[i+2]:
                        graph[i]-=(graph[i+1]-graph[i+2])
                        tot+=(graph[i+1]-graph[i+2])*(n+m)
                        graph[i+1]=graph[i+2]
                    else:
                        tot+=graph[i]*(n+m)
                        graph[i+1]-=graph[i]
                        graph[i]=0
                else:
                    d=min(graph[i],graph[i+1],graph[i+2])
                    tot+=d*(n+m+m)
                    graph[i]-=d
                    graph[i+1]-=d
                    graph[i+2]-=d
            elif graph[i+1]!=0 and graph[i+2]==0:
                d=min(graph[i+1],graph[i])
                tot+=d*(n+m)
                graph[i+1]-=d
                graph[i]-=d
            else:
                tot+=n*graph[i]
                graph[i]=0
print(tot)