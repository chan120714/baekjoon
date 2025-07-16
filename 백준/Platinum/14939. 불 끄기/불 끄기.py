import sys
input=sys.stdin.readline
from itertools import combinations
p=[i for i in range(10)]
a=[list(map(str,input().rstrip())) for i in range(10)]
def rev(x,y,n):
    if n[x][y]=='#':
        n[x][y]='O'
    else:
        n[x][y]='#'
    for i in ((1,0),(-1,0),(0,1),(0,-1)):
        dx=x+i[0]
        dy=y+i[1]
        if dx<0 or dy<0 or dx>=10 or dy>=10:
            continue
        if n[dx][dy]=='#':
            n[dx][dy]='O'
        else:
            n[dx][dy]='#'
    return n
res=101
def sol(n):
    cur=0
    for i in range(1,10):
        for j in range(10):
            if n[i-1][j]=='O':
                cur+=1
                for k in ((1,0),(-1,0),(0,1),(0,-1),(0,0)):
                    dx=i+k[0]
                    dy=j+k[1]
                    if dx<0 or dy<0 or dx>=10 or dy>=10:
                        continue
                    if n[dx][dy]=='#':
                        n[dx][dy]='O'
                    else:
                        n[dx][dy]='#'
    for i in n:
        if 'O' in i:
            return 10000
    return cur
for i in range(11):
    for j in combinations(p,i):
        n=[a[i].copy()for i in range(10)]
        for k in j:
            if n[0][k]=='#':
                n[0][k]='O'
            else:
                n[0][k]='#'
            for v in ((1,0),(-1,0),(0,1),(0,-1)):
                dx=v[0]
                dy=k+v[1]
                if dx<0 or dy<0 or dx>=10 or dy>=10:
                    continue
                if n[dx][dy]=='#':
                    n[dx][dy]='O'
                else:
                    n[dx][dy]='#'
        res=min(i+sol(n),res)
print(res)