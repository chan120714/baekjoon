import sys
input=sys.stdin.readline
a=int(input())
graph=[list(map(int,input().split())) for i in range(a)]

def colo(a,r,c):
    b,w=0,0
    for i in range(r,r+a):
        for j in range(c,c+a):
            if graph[i][j]==1:
                b+=1
            else:
                w+=1
    if w==0 and b>0:
        return 1
    if w>0 and b==0:
        return 100000
    else:
        return colo(a//2,r,c)+colo(a//2,a//2+r,c)+colo(a//2,r,c+a//2)+colo(a//2,a//2+r,c+a//2)
k=colo(a,0,0)
print(k//100000)
print(k%100000)