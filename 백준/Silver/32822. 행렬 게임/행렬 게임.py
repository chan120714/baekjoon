import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    b.append(list(map(int,input().split())))

p=[0]*2432

for i in range(n):
    for j in range(n):
        p[i]=max(p[i],abs(a[j][i]-b[j][i]))

res=0
for i in list(map(int,input().split())):
    res+=p[i-1]
print(res)
