import sys
input=sys.stdin.readline
n,m=map(int,input().split())
w_1=[list(map(int,input().split())) for i in range(n)]
a,b=map(int,input().split())
w_2=[list(map(int,input().split())) for i in range(a)]
for i in range(n):
    for j in range(b):
        s=0
        for k in range(a):
            s+=w_1[i][k]*w_2[k][j]
        print(s,end=' ')
    print()