import sys
input=sys.stdin.readline
n,m=map(int,input().split())
w=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        w[i][j]%=1000
def pow(n,m,w):
    if m==1:
        return w
    elif m%2==0:
        x=pow(n,m//2,w)
        s=[[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            for j in range(n):
                k=0
                for l in range(n):
                    k+=x[i][l]*x[l][j]%1000
                s[i][j]=k%1000
        return s
    else:
        x=pow(n,m//2,w)
        r=[[0 for i in range(n)]for j in range(n)]
        s=[[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            for j in range(n):
                k=0
                for l in range(n):
                    k+=x[i][l]*x[l][j]%1000
                r[i][j]=k%1000
        for i in range(n):
            for j in range(n):
                k=0
                for l in range(n):
                    k+=w[i][l]*r[l][j]%1000
                s[i][j]=k%1000
        return s
a=pow(n,m,w)
for i in a:
    print(*i)