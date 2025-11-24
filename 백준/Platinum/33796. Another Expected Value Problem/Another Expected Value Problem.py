import sys
input=sys.stdin.readline
for __ in range(int(input())):
    n,k=map(int,input().split())
    print(sum(map(int,input().split()))*pow(n,-1,M:=10**9+7)%M)