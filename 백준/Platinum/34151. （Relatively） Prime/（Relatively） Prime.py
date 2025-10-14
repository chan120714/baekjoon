import sys
input=sys.stdin.readline
MOD=998244353
for i in range(int(input())):
    p,n,m=map(int,input().split())
    print(pow(p,min(n,m),MOD))
