import sys
input=sys.stdin.readline
a,b=map(int,input().split())
c=list(map(int,input().split()))
e=[0]
f=[]
d=0
for i in range(a):
    d+=c[i]
    e.append(d)
for i in range(a-b+1):
    f.append(e[i+b]-e[i])

print(max(f))