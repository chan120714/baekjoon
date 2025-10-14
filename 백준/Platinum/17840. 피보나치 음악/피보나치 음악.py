import sys
input=sys.stdin.readline
def pisano(x):
    a,b=0,1
    t=1
    for i in range(x**2):
        a,b=b,(a+b)%x
        if a==0 and b==1:return t
        t+=1
n,m=map(int,input().split())
x=pisano(m)
b=[0,1]
t='01'
for i in range(x-2):
    b.append((b[i]+b[i+1])%m)
    t+=str(b[i+2])
for i in range(n):
    a=int(input())
    print(t[a%len(t)])
