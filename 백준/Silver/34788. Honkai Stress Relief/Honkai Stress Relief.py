import sys
input=sys.stdin.readline

n,a,b=map(int,input().split())
T=1
for i in range(n):
    s,e=map(int,input().split())
    V=b-a
    K=min(e,b)-max(s,a)
    if (K<0):
        K=0
    T*=K/V
print(1-T)