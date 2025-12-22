import sys
input=sys.stdin.readline

n=int(input())
a=[input().rstrip() for i in range(n)]

tree=[0]*312121

def update(x):
    while x<=n:
        tree[x]+=1
        x+=x&-x

def q(x):
    r=0
    while x:
        r+=tree[x]
        x-=x&-x
    return r

a.sort()

b=[(a[i][::-1],i+1) for i in range(n)]
b.sort()

res=0
for x,i in enumerate(b,1):
    update(i[1])
    res+=x-q(i[1])
    

print(res)