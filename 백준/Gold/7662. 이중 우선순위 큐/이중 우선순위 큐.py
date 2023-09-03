import sys
input=sys.stdin.readline
from heapq import*
a=int(input())
for _ in range(a):
    n=int(input())
    visit=[0]*(n+1)
    minh=[]
    maxh=[]
    for i in range(n):
        q,w=map(str,input().split())
        w=int(w)
        if q=='I':
            heappush(minh,(w,i))
            heappush(maxh,(-w,i))
            visit[i]=1
        else:
            if w==1:
                while maxh:
                    if visit[maxh[0][1]]==0:
                        heappop(maxh)
                    else:
                        break
                if maxh:
                    visit[heappop(maxh)[1]]=0
            else:
                while minh:
                    if visit[minh[0][1]]==0:
                        heappop(minh)
                    else:
                        break
                if minh:
                    visit[heappop(minh)[1]]=0
    while minh:
        if visit[minh[0][1]]==0:
            heappop(minh)
        else:
            break
    while maxh:
        if visit[maxh[0][1]]==0:
            heappop(maxh)
        else:
            break
    if len(maxh)+len(minh)==0:
        print("EMPTY")
        continue
    print(-maxh[0][0],minh[0][0])