import sys
input=sys.stdin.readline
n,m=map(int,input().split())
k=list(map(int,input().split()))
k.sort()
s=1
t=k[0]
for i in k[1:]:
    if (i-t+1)>m:
        s+=1
        t=i
print(s)