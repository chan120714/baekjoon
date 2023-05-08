import sys
input=sys.stdin.readline

def bin(x1):
    x=0
    for i in range(a):
        for j in range(b):
            if n[i][j]>x1:
                x+=(2*(n[i][j]-x1))
            if n[i][j]<x1:
                x+=x1-n[i][j]
    return (x,x1)

a,b,c=map(int,input().split())
n=[list(map(int,input().split())) for i in range(a)]
res=[float('inf'),0]
x1=c

for i in range(a):
    for j in range(b):
        x1+= n[i][j]
        
x2=min(257,(x1//(a*b))+1)

for i in range(x2):
    t,h=bin(i)
    if t<=res[0]:
        res[0]=t
        if h>res[1]:
            res[1]=h
print(*res)