import sys
input=sys.stdin.readline
a=int(input())
g=sorted([int(input()) for i in range(a)])
res=0
for i in range(a):
    res+=abs(g[i]-i-1)
print(res)