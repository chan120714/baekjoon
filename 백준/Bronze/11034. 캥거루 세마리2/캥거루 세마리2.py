import sys
input=sys.stdin.readline
while True:
    try:
        n,m,k=map(int,input().split())
        print(max(m-n-1,k-m-1))
    except:
        break