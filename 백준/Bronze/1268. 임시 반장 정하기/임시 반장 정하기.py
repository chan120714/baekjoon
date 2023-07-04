import sys
input=sys.stdin.readline
a=int(input())
b=[list(map(int,input().split())) for i in range(a)]
m=0
s=0
for i in range(a):
    n=[0]*a
    for j in range(5):
        for k in range(a):
            if i==k:
                continue
            if b[i][j]==b[k][j]:
                n[k]=1
    if m<sum(n):
        s=i
        m=sum(n)
print(s+1)